import cv2


video_path = 'sample_video.mp4'
cap = cv2.VideoCapture(video_path)


if not cap.isOpened():
    print("Error: Couldn't open video file.")
    exit()


ret, frame = cap.read()
if not ret:
    print("Error: Couldn't read the first frame.")
    exit()


bbox = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select Object to Track")


tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    success, bbox = tracker.update(frame)

    if success:
       
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

   
    cv2.imshow("Object Tracking", frame)

    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
