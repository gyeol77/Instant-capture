import cv2
camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None

recording = False
flip_horizontal = False

while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        break

    if flip_horizontal:
        frame = cv2.flip(frame, 1)

    if recording and out is None:
        filename = "new_video.avi"
        out = cv2.VideoWriter(filename, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    
    if recording and out is not None:
        out.write(frame)
        
        cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)
    
    cv2.imshow('Video Recorder', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == 32:
        recording = not recording
        if not recording and out is not None:
            out.release()
            out = None
    elif key == ord('t') or key == ord('T'):
        flip_horizontal = not flip_horizontal

camera.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()
