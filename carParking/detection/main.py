import os
from ultralyticsplus import YOLO
import cv2 as cv
from carParking.detection.utils.extract_bounding_boxes import extract_parking_spots
from  carParking.detection.utils.detect_car import detect_cars
from  carParking.detection.utils.detect_car import detect_track_cars
from carParking.detection.utils.info_drawer_utils import draw_info_detect,draw_info_track
from  carParking.detection.utils.spot_statuses import update_spot_statuses_track
from  carParking.detection.utils.spot_statuses import update_spot_statuses
from  carParking.detection.utils.spot_statuses import calc_diff
import numpy as np

def Detect(selected_model) :
    # Chemins des fichiers*
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    MASK_PATH = f'{basedir}/tools/mask2.png'
    VIDEO_PATH = f'{basedir}/videos/parking2.mp4'
    UPDATE_INTERVAL = 20

    # Charger le masque des places de parking
    image_mask = cv.imread(MASK_PATH, 0)
    parking_spots = extract_parking_spots(image_mask)
    cap = cv.VideoCapture(VIDEO_PATH)
    # Initialiser le mod�le YOLO
    if(selected_model == "yolov8"):
        model = YOLO(f'{basedir}/tools/best.pt')

    # Variables
    number_frames = 0
    occupied_spots = 0
    spot_statuses = [0] * len(parking_spots)
    diffs = [0] * len(parking_spots)
    previous_frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video.")
            break
        if number_frames % UPDATE_INTERVAL == 0:
            if previous_frame is None:
                arr_ = list(range(len(parking_spots)))
            else:
                max_diff = np.amax(diffs)
                arr_ = [j for j in np.argsort(diffs) if max_diff != 0 and diffs[j] / max_diff > 0.4]
            #print(arr_)
        
            boxes = detect_cars(frame,model)
            spot_statuses = update_spot_statuses(boxes, parking_spots, arr_,spot_statuses)
            occupied_spots = sum(spot_statuses)
                
                
        #calcule de la diffrence entre deux frame
        if number_frames % UPDATE_INTERVAL == 0 and previous_frame is not None:
            for i, spot in enumerate(parking_spots):
                spot_x1, spot_y1, spot_x2, spot_y2,id = spot
                spot_crop = frame[spot_y1:spot_y2, spot_x1:spot_x2, :]
                prev_spot_crop = previous_frame[spot_y1:spot_y2, spot_x1:spot_x2, :]
                diffs[i] = calc_diff(spot_crop, prev_spot_crop)
            #print([diffs[j] for j in np.argsort(diffs)][::-1])

    
        previous_frame = frame.copy()
        
        frame = draw_info_detect(frame,parking_spots,spot_statuses,occupied_spots,len(boxes))

        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


        number_frames += 1

    cap.release()
    cv.destroyAllWindows()
    
def DetectTrack(selected_model,selected_tracker):
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # Chemins des fichiers
    MASK_PATH = f'{basedir}/tools/mask2.png'
    VIDEO_PATH = f'{basedir}/videos/parking2.mp4'
    UPDATE_INTERVAL = 200

    # Charger le masque des places de parking
    image_mask = cv.imread(MASK_PATH, 0)
    parking_spots = extract_parking_spots(image_mask)
    cap = cv.VideoCapture(VIDEO_PATH)

    # Initialiser le modèle YOLO
    if(selected_model == "yolov8"):
         model = YOLO(f'{basedir}/tools/best.pt')
         tracker = selected_tracker+".yaml"

    # main
    number_frames = 0
    occupied_spots = 0
    spot_statuses = [0] * len(parking_spots)
    diffs = [0] * len(parking_spots)
    previous_frame = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video.")
            break
        if number_frames % UPDATE_INTERVAL == 0:
            if previous_frame is None:
                arr_ = list(range(len(parking_spots)))
            else:
                max_diff = np.amax(diffs)
                arr_ = [j for j in np.argsort(diffs) if max_diff != 0 and diffs[j] / max_diff > 0.4]
        
            boxes = detect_track_cars(frame, model,tracker)
            spot_statuses = update_spot_statuses_track(boxes, parking_spots, arr_,spot_statuses)
            occupied_spots = sum(spot_statuses)
                
        #calcule de la diffrence entre deux frame
        if number_frames % UPDATE_INTERVAL == 0 and previous_frame is not None:
            for i, spot in enumerate(parking_spots):
                spot_x1, spot_y1, spot_x2, spot_y2,id = spot
                spot_crop = frame[spot_y1:spot_y2, spot_x1:spot_x2, :]
                prev_spot_crop = previous_frame[spot_y1:spot_y2, spot_x1:spot_x2, :]
                diffs[i] = calc_diff(spot_crop, prev_spot_crop)
            #print([diffs[j] for j in np.argsort(diffs)][::-1])

    
        previous_frame = frame.copy()


        cv.putText(frame, f'Occupancy: {occupied_spots}/{len(parking_spots)}',
                   (50, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        frame = draw_info_track(frame,parking_spots,spot_statuses,occupied_spots,len(boxes),boxes)
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


        number_frames += 1

    cap.release()
    cv.destroyAllWindows()