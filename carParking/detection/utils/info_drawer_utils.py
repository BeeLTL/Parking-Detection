import cv2 as cv
def draw_info_detect(frame,parking_spots,spot_statuses,occupied_spots,number_cars):
        free_spot_ids = [spot_id for spot, status, spot_id in zip(parking_spots, spot_statuses, [i[4] for i in parking_spots]) if status == 0]    
        occupied_spot_ids = [spot_id for spot, status, spot_id in zip(parking_spots, spot_statuses, [i[4] for i in parking_spots]) if status == 1]    
            # Dessiner les boites
        for i, spot in enumerate(parking_spots):
            spot_x1, spot_y1, spot_x2, spot_y2, spot_id = spot

            if spot_statuses[i] == 1:
                
                cv.rectangle(frame, (spot_x1, spot_y1), (spot_x2, spot_y2), (0, 0, 255), 2)
                cv.putText(frame, f'Spot {spot_id}', (spot_x1 + 10, spot_y1 + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5,  (0, 0, 255), 2)
            else:
                cv.rectangle(frame, (spot_x1, spot_y1), (spot_x2, spot_y2), (0, 255, 0), 2)
                cv.putText(frame, f'Spot {spot_id}', (spot_x1 + 10, spot_y1 + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5,  (0, 255, 0), 2)
                
            # Add the spot number on top of the rectangle
        cv.putText(frame, f'{i+1}', (spot_x1 + 10, spot_y1 + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Create a semi-transparent rectangle
        overlay = frame.copy()
        width=2000
        height=105
        start_x = 40
        start_y = 0
        end_x = 260+width
        end_y = 60+height
        cv.rectangle(overlay, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
        alpha = 0.5 
        cv.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

        # Draw the text on top of the rectangle
        cv.putText(frame, f'Total Parking Spots: {len(parking_spots)}',
                 (start_x, start_y+30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv.putText(frame, f'Occupancy: {occupied_spots}/{len(parking_spots)}',
                   (start_x, start_y+60), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)   
        cv.putText(frame, f'vehicles Detected in the frame by the model: {number_cars}',
                   (start_x, start_y+90), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv.putText(frame, f'Free Spots: {free_spot_ids}',
                   (start_x, start_y+120), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv.putText(frame, f'Occupied Spots: {occupied_spot_ids}',
                   (start_x, start_y+150), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        output_video_frames = cv.imencode('.JPEG', frame,[cv.IMWRITE_JPEG_QUALITY,50])[1].tobytes()
    
        return output_video_frames

def draw_info_track(frame,parking_spots,spot_statuses,occupied_spots,number_cars,boxes):
        free_spot_ids = [spot_id for spot, status, spot_id in zip(parking_spots, spot_statuses, [i[4] for i in parking_spots]) if status == 0]    
        occupied_spot_ids = [spot_id for spot, status, spot_id in zip(parking_spots, spot_statuses, [i[4] for i in parking_spots]) if status == 1]   
        
        for box in boxes:
            car_x1, car_y1, car_x2, car_y2, track_id = box
            car_center_x = (car_x1 + car_x2) // 2
            car_center_y = (car_y1 + car_y2) // 2
            cv.putText(frame, f' {int(track_id)}', (int(car_center_x), int(car_center_y) ),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            # Dessiner les boites
        for i, spot in enumerate(parking_spots):
            spot_x1, spot_y1, spot_x2, spot_y2, spot_id = spot

            if spot_statuses[i] == 1:
                
                cv.rectangle(frame, (spot_x1, spot_y1), (spot_x2, spot_y2), (0, 0, 255), 2)
                cv.putText(frame, f'Spot {spot_id}', (spot_x1 + 10, spot_y1 + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5,  (0, 0, 255), 2)
            else:
                cv.rectangle(frame, (spot_x1, spot_y1), (spot_x2, spot_y2), (0, 255, 0), 2)
                cv.putText(frame, f'Spot {spot_id}', (spot_x1 + 10, spot_y1 + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5,  (0, 255, 0), 2)
                
            # Add the spot number on top of the rectangle
        cv.putText(frame, f'{i+1}', (spot_x1 + 10, spot_y1 + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Create a semi-transparent rectangle
        overlay = frame.copy()
        width=2000
        height=105
        start_x = 40
        start_y = 0
        end_x = 260+width
        end_y = 60+height
        cv.rectangle(overlay, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
        alpha = 0.5 
        cv.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

        # Draw the text on top of the rectangle
        cv.putText(frame, f'Total Parking Spots: {len(parking_spots)}',
                 (start_x, start_y+30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv.putText(frame, f'Occupancy: {occupied_spots}/{len(parking_spots)}',
                   (start_x, start_y+60), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)   
        cv.putText(frame, f'vehicles Detected in the frame by the model: {number_cars}',
                   (start_x, start_y+90), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv.putText(frame, f'Free Spots: {free_spot_ids}',
                   (start_x, start_y+120), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv.putText(frame, f'Occupied Spots: {occupied_spot_ids}',
                   (start_x, start_y+150), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        output_video_frames = cv.imencode('.JPEG', frame,[cv.IMWRITE_JPEG_QUALITY,50])[1].tobytes()
    
        return output_video_frames