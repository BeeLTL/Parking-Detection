import numpy as np
import cv2 as cv

# Fonction pour mettre à jour les statuts des places de parking
def update_spot_statuses(boxes, parking_spots, changed_spot_indices,spot_statuses):
    for idx in changed_spot_indices:
        spot = parking_spots[idx]
        points = np.array([[spot[0], spot[1]], [spot[2], spot[1]], [spot[2], spot[3]], [spot[0], spot[3]]])
        for box in boxes:
            car_x1, car_y1, car_x2, car_y2 = box
            car_center_x = int(car_x1 + car_x2) // 2
            car_center_y = int(car_y1 + car_y2) // 2
            if cv.pointPolygonTest(points, ((car_center_x, car_center_y)), False) >= 0:
                spot_statuses[idx] = 1
                break
    return spot_statuses

# Fonction pour mettre à jour les statuts des places de parking
def update_spot_statuses_track(boxes, parking_spots, changed_spot_indices, spot_statuses):
    for idx in changed_spot_indices:
        spot = parking_spots[idx]
        points = np.array([[spot[0], spot[1]], [spot[2], spot[1]], [spot[2], spot[3]], [spot[0], spot[3]]])
        for box in boxes:
            car_x1, car_y1, car_x2, car_y2, track_id = box
            car_center_x = int(car_x1 + car_x2) // 2
            car_center_y = int(car_y1 + car_y2) // 2
            if cv.pointPolygonTest(points, ((car_center_x, car_center_y)), False) >= 0:
                spot_statuses[idx] = 1
                break
    return spot_statuses


# Fonction pour calculer la différence entre deux images pour eviter de redessiner toutes les boites
def calc_diff(im1, im2):
    return np.abs(np.mean(im1) - np.mean(im2))