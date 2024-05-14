from flask import Flask, request, jsonify
import cv2
from Detector import YOLOV5_Detector

app = Flask(__name__)

@app.route('/detect_objects', methods=['POST'])
def detect_objects():
    # Verifica si se envió un archivo de video
    if 'video' not in request.files:
        return jsonify({'error': 'No se ha proporcionado ningún archivo de video'}), 400

    video_file = request.files['video']

    # Guarda el archivo de video temporalmente
    video_path = 'temp_video.mp4'
    video_file.save(video_path)

    # Inicializa el detector
    detector = YOLOV5_Detector(weights='best.pt',
                               img_size=640,
                               confidence_thres=0.3,
                               iou_thresh=0.45,
                               agnostic_nms=True,
                               augment=True)

    # Abre el archivo de video
    vid = cv2.VideoCapture(video_path)
    detections = []

    while True:
        ret, frame = vid.read()
        if ret:
            # Detecta objetos en el frame actual
            res = detector.Detect(frame)
            # Guarda los resultados de detección
            detections.append(res)

        else:
            break

    # Limpia y cierra el video
    vid.release()
    cv2.destroyAllWindows()

    # Procesa los resultados de detección y devuelve los tiempos de aparición
    # Esto es un ejemplo, deberás ajustarlo según la estructura de tus resultados
    objects_appearance_times = process_detections(detections)

    return jsonify(objects_appearance_times)

def process_detections(detections):
    # Aquí deberás procesar los resultados de detección para extraer los tiempos de aparición
    # de cada objeto a lo largo del video
    # Puedes ajustar esta función según la estructura de tus resultados de detección
    # Esto es solo un ejemplo
    objects_appearance_times = {'object1': [0, 3, 7], 'object2': [1, 4, 8]} # Ejemplo de salida
    return objects_appearance_times

if __name__ == '__main__':
    app.run(debug=True)
