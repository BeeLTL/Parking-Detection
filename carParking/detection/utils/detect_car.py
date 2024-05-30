import numpy as np
from ultralyticsplus import YOLO, render_result

# Fonction pour détecter les voitures
def detect_cars(frame,model):
    
    results = model.predict(frame,classes=[3,4,5,8])
    boxes = np.squeeze(results[0].boxes.xyxy)
    return boxes

# Fonction pour détecter les voitures la diff l'ajout des id pour quil soit toujours suivi / connu 
def detect_track_cars(frame, model,tracker):
    results = model.track(frame, persist=True, tracker=tracker)
    boxes = np.squeeze(results[0].boxes.xyxy)
    track_ids = results[0].boxes.id.int().cpu().tolist()

    boxes_with_ids = []
    for box, track_id in zip(boxes, track_ids):
        box_with_id = np.append(box, track_id)
        boxes_with_ids.append(box_with_id)

    return np.array(boxes_with_ids)