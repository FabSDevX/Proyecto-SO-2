import multiprocessing
import os
import tempfile
from flask import Blueprint, jsonify, request
from azure.storage.blob import BlobServiceClient
import requests
from .utils import obtain_video_duration, guardar_partes, detectar_persona, mayus_separation

routes = Blueprint('routes', __name__)

CONNECTION_STRING = os.getenv('CONNECTION_STRING')
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
YT_API_KEY = os.getenv('YT_API_KEY')

blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_name = "uploaded-movies"

@routes.route('/', methods=['GET'])
def index():
    return "Hello World!"
    

def download_video(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Video downloaded successfully: {filename}")
    else:
        print(f"Failed to download video: {response.status_code}")

def list_blobs_in_container():

    container_client = blob_service_client.get_container_client(container_name)

    # List all blobs in the container
    blob_list = container_client.list_blobs()

    blob_names = [blob.name for blob in blob_list]
    blob_count = len(blob_names)

    return blob_names, blob_count




@routes.route('/obtener_elementos', methods=['GET'])
def obtener_elementos():
    try:
        blob_names, blob_count = list_blobs_in_container()
        
        return jsonify({
            'blobs' : blob_names,
            'count' : blob_count
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@routes.route('/procesar_pelicula', methods=['POST'])
def procesar_pelicula():
    if request.method == 'POST':


        video_url = request.form.get('url_pelicula')
        if not video_url:
            return "No URL provided", 400

        
        num_cpus = abs(multiprocessing.cpu_count() - 3)
        if(num_cpus==0):num_cpus=1
        elif(num_cpus>=6):num_cpus=5

        
        video_filename = 'TemporalVideo.mp4'

        # Descargar el video desde la URL
        download_video(video_url, video_filename)

        duration = obtain_video_duration(video_filename)

        movie_cuts = duration / num_cpus
       
        cuts = [(i * movie_cuts, (i + 1) * movie_cuts if i < num_cpus - 1 else duration) for i in range(num_cpus)]

        guardar_partes(video_filename, cuts)

        os.remove(video_filename)

        filenames = []
        index = 0
        while index < num_cpus:
            filenames.append("parte_"+ str(index)+ ".mp4")
            index = index + 1

        detectar_persona(filenames)

        for x in filenames:
            os.remove(x)

        return "Video succesfully"
    else:
        return "Invalid Request"

def upload_to_blob(container_name, file_path, blob_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    print(f"File {file_path} uploaded to blob {blob_name} in container {container_name}.")

@routes.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        # Save the file to a temporary location
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, file.filename)
        file.save(temp_file_path)
        
        # Upload the file to Azure Blob Storage
        try:
            upload_to_blob(container_name, temp_file_path, file.filename)
            return jsonify({'message': f"File {file.filename} uploaded successfully."}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            # Clean up temporary file
            os.remove(temp_file_path)

'''
TMBD: https://www.themoviedb.org/ API for search a movie name and web name, description and image
Youtube Data API v3: https://developers.google.com/youtube/v3/docs?apix=true&hl=es-419 API for search a YT video and get name, description and image

This route search a upload video to get certain details that can be showen in front-end
'''
@routes.route('/search_movie', methods=['GET'])
def search_movie():
    video_name = request.args.get('name')
    if not video_name:
        return jsonify({'error': 'No movie name provided'}), 400
    video_name = mayus_separation(video_name) #MessiMates --> Messi Mates
    search_url_tmbl = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': TMDB_API_KEY,
        'query': video_name
    }
    
    response = requests.get(search_url_tmbl, params=params)
    data = response.json()
    try:
        if data['results']:
            entire_data = data['results'][0]

            movie_details = {'title': entire_data['title'],
                            'description': entire_data['overview'],
                            'poster_url': "https://image.tmdb.org/t/p/w500" + entire_data['poster_path']}
        else:
            search_url_yt = 'https://www.googleapis.com/youtube/v3/search'
            params = {
                'part': 'snippet',
                'q': video_name,
                'type': 'video',
                'key': YT_API_KEY
            }
            response = requests.get(search_url_yt, params=params)
            data = response.json()
            if not data.get('items'):
                return jsonify({'error': 'No video found'}), 404
            entire_data = data['items'][0]['snippet']
            thumbnails = entire_data['thumbnails']
            largest_thumbnail = max(thumbnails.values(), key=lambda t: t['height'])
            print(entire_data)
            movie_details = {'title': entire_data['title'],
                            'description': entire_data['description'],
                            'poster_url': largest_thumbnail['url']}
    except:
        return jsonify({'error': 'Request error'}), 404
    
    return jsonify(movie_details)
