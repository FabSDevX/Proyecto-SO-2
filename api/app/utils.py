from moviepy.editor import VideoFileClip
import multiprocessing
import math
import cv2
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