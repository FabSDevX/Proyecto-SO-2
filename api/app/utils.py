from moviepy.editor import VideoFileClip
from .simple_facerec import SimpleFacerec
import multiprocessing
import math
import cv2
import concurrent.futures

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

def process_video(video_path, sfr, result_queue):

    cap = cv2.VideoCapture(video_path)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    frame_count = 0
    detected_frames_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 6 == 0:
            flag = sfr.detect_known_faces(frame)
            if flag:
                detected_frames_count += 1
                print(f"{video_path}: {detected_frames_count}")

        frame_count += 1

    cap.release()
    result_queue.put(detected_frames_count)

def detectar_persona(video_files):

    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    total_detected_frames_count = 0
    
    result_queue = multiprocessing.Queue()
    processes = []

    for video_name in video_files:
        print(video_name)
        process = multiprocessing.Process(target=process_video, args=(video_name, sfr, result_queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

    total_detected_frames_count = 0
    while not result_queue.empty():
        total_detected_frames_count += result_queue.get()

    print("Total detected frames:", total_detected_frames_count)

    cap = cv2.VideoCapture(video_files[0])
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)
    seconds_per_frame = 1/fps

    print("Total seconds {:.3f}".format((total_detected_frames_count * 6) * seconds_per_frame))

    