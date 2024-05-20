import multiprocessing
import os
import tempfile
from flask import Blueprint, jsonify, request
from .utils import obtain_video_duration,cut_video,guardar_partes, guardar_parte
from azure.storage.blob import BlobServiceClient
import requests

routes = Blueprint('routes', __name__)

CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=describedmovies;AccountKey=Devf95Gu9WKLbO21qcLQCLztqSYK6Nqrtcnnx/iqrYEXMY/KOwb8kh3QmHWNMbVXSAoAb4GSoXtc+ASty8F0Ww==;EndpointSuffix=core.windows.net"

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
        
        video_filename = 'MessiMates.mp4'

        # Descargar el video desde la URL
        download_video(video_url, video_filename)


        #num_cpus = abs(multiprocessing.cpu_count() - 3)
        #print(num_cpus)
        #if(num_cpus==0):num_cpus=1

        num_cpus = 3

        duration = obtain_video_duration(video_filename)

        #print(duration)

        movie_cuts = duration / num_cpus
        # minuts_movie = []
        # for x in range(num_cpus):
        #     if not minuts_movie:
        #         minuts_movie.append((0,movie_cuts * 60))
        #     else:
        #         minuts_movie.append((minuts_movie[x-1][1],minuts_movie[x-1][1] + (movie_cuts*60)))
       
        processes = []
        for i in range(num_cpus):
            start = i * movie_cuts
            end = start + movie_cuts if i < num_cpus - 1 else duration
            process = multiprocessing.Process(target=guardar_parte, args=(video_filename, start, end))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        os.remove(video_filename)

        return "Video succesfully"
    else:
        return "Invalid Request"


