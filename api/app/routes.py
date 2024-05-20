import multiprocessing
from flask import Blueprint, request
from .utils import obtain_video_duration, guardar_partes

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def index():
    return "Hello World!"

@routes.route('/procesar_pelicula', methods=['POST'])
def procesar_pelicula():
    if request.method == 'POST' and 'archivo_pelicula' in request.files:

        movie = request.files['archivo_pelicula']
        num_cpus = abs(multiprocessing.cpu_count() - 3)
        if(num_cpus==0):num_cpus=1
        elif(num_cpus>=6):num_cpus=5
        movie_name = movie.filename
        
        movie.save(movie_name)
        duration = obtain_video_duration(movie_name)
        movie_cuts = duration / num_cpus
       
        cuts = [(i * movie_cuts, (i + 1) * movie_cuts if i < num_cpus - 1 else duration) for i in range(num_cpus)]

        guardar_partes(movie_name, cuts)

        return "Video succesfully"
    else:
        return "Invalid Request"