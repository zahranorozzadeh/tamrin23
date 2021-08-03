import cv2
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
my_video = cv2.VideoCapture(0)
while True:
    validation, frame = my_video.read()
    if validation is not True:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    row, cols = frame_gray.shape
    half_frame = frame_gray[:, 0:cols//2]
    flipped_half_frame = cv2.flip(half_frame, 1)
    frame_gray[:, cols//2:] = flipped_half_frame

    # faces = face_detector.detectMultiScale(frame_gray, 1.3)
    # frame = cv2.resize(frame, (800, 600))
    # for i, face in enumerate(faces):
    #     x, y, w, h = face
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 8)

    cv2.imshow('output', frame_gray)
    cv2.waitKey(10)