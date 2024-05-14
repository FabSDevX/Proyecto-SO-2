from moviepy.editor import VideoFileClip
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
    
def guardar_partes(nombre_archivo, cuts):
    cap = cv2.VideoCapture(nombre_archivo)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    for i, cut in enumerate(cuts):
        start_time, end_time = cut
        cap.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)
        out = cv2.VideoWriter(f'parte_{i}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
        while cap.isOpened() and cap.get(cv2.CAP_PROP_POS_MSEC) <= end_time * 1000:
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            else:
                break
        out.release()

    cap.release()
    cv2.destroyAllWindows()