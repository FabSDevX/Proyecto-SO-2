import multiprocessing
from flask import Blueprint, request
from .utils import obtain_video_duration,cut_video,guardar_partes, guardar_parte

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
        movie_name = movie.filename
        
        movie.save(movie_name)
        duration = obtain_video_duration(movie_name)
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
            process = multiprocessing.Process(target=guardar_parte, args=(movie_name, start, end))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        return "Video succesfully"
    else:
        return "Invalid Request"