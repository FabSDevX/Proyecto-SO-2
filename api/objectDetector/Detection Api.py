import os
from flask import Flask, request, jsonify
import cv2
from Detector import YOLOV5_Detector

app = Flask(__name__)

@app.route('/detect_objects', methods=['POST'])
def detect_objects():
    # Obtener el archivo de video del cuerpo de la solicitud
    file = request.files['video']
    
    # Guardar el archivo temporalmente
    file_path = 'temp_video.mp4'
    file.save(file_path)
    
    # Inicializar el detector
    detector = YOLOV5_Detector(weights='as.pt',
                               img_size=640,
                               confidence_thres=0.3,
                               iou_thresh=0.45,
                               agnostic_nms=True,
                               augment=True)
    
    # Iniciar la detección en el video
    vid = cv2.VideoCapture(file_path)
    fps = vid.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    counts = {}
    while True:
        ret, frame = vid.read()
        if ret:
            frame_count+=1
            res = detector.Detect(frame)
            counts.update(detector.get_counts())
        else:
            break
    
    vid.release()
    cv2.destroyAllWindows()
    
    # Eliminar el archivo temporal
    os.remove(file_path)
    
    # Devolver los conteos acumulados como respuesta
    print(fps)
    print(frame_count)
    return jsonify(counts)

if __name__ == '__main__':
    app.run(debug=True)
