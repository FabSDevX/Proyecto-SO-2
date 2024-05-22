from moviepy.editor import VideoFileClip
from .simple_facerec import SimpleFacerec
import multiprocessing
import math
import cv2
import concurrent.futures
import re

def obtain_video_duration(file):
    video = VideoFileClip(file)
    duration = math.floor(video.duration) / 60
    video.close()
    return duration

def cut_video(file, cuts):
    video = VideoFileClip(file)
    parts = []
    for begin, end in cuts:
        part = video.subclip(begin, end)
        parts.append(part)
    video.close()
    return parts

def guardar_parte(movie_path, start, end):
    guardar_partes(movie_path, [(start, end)])
    
def guardar_parte(movie_path, start, end, index):
    cap = cv2.VideoCapture(movie_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    cap.set(cv2.CAP_PROP_POS_MSEC, (start * 60) * 1000 )
    out = cv2.VideoWriter(f'parte_{index}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
    while cap.isOpened() and cap.get(cv2.CAP_PROP_POS_MSEC) <= (end * 60) * 1000:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
    out.release()
    cap.release()

def guardar_partes(nombre_archivo, cuts):
    processes = []
    for i, (start, end) in enumerate(cuts):
        process = multiprocessing.Process(target=guardar_parte, args=(nombre_archivo, start, end, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

def process_video(video_path, sfr, result_queue, result_objects_queue,detector):

    cap = cv2.VideoCapture(video_path)
        
    frame_count = 0
    detected_frames_count = 0
    counts = {}
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % 6 == 0:
            detector.Detect(frame)
            flag = sfr.detect_known_faces(frame)
            counts.update(detector.get_counts())
            # cv2.imshow("Detection", res)
            # key = cv2.waitKey(1)
            # if key == ord('q'):
            #     break
            if flag:
                detected_frames_count += 1
        frame_count += 1
    cap.release()
    result_objects_queue.put(counts)
    result_queue.put(detected_frames_count)

def detectar_persona(video_files,name,detector):

    sfr = SimpleFacerec()
    if(name == "leonelMessi"):
        sfr.load_encoding_images("dataset/messi/")
    elif( name== "johnKrasinski"):
        sfr.load_encoding_images("dataset/john/")
    total_detected_frames_count = 0
    
    result_queue = multiprocessing.Queue()
    result_objects_queue = multiprocessing.Queue()
    processes = []

    for video_name in video_files:
        process = multiprocessing.Process(target=process_video, args=(video_name, sfr, result_queue, result_objects_queue,detector))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

    total_detected_frames_count = 0
    while not result_queue.empty():
        total_detected_frames_count += result_queue.get()

    knife = 0
    glasses = 0
    counts = {}
    while not result_objects_queue.empty():
        result = result_objects_queue.get()
        knife += result['knife']
        glasses += result['glasses']
        
    counts['knife'] = knife * 6
    counts['glasses'] = glasses * 6
    counts[name] = total_detected_frames_count * 6

    return counts
"""
Example:
"Messi"
"MessiMates"
"UnLugarEnSilencio"

Returns:
"Messi"
"Messi Mates"
"Un Lugar En Silencio"
"""
def mayus_separation(texto : str):
    texto = texto.split('.')[0]
    # Use a regular expression to separate the uppercase letters
    separation_words= re.findall('[A-Z][^A-Z]*', texto)
    # Join Words
    response = ' '.join(separation_words)
    return response