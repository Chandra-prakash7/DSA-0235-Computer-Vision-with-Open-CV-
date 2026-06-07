import cv2
import os

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

if face_cascade.empty():
    raise FileNotFoundError("Unable to load Haar cascade file.")

image_path = "LIST OF EXPERIMENTS/exp33/exp33.jpg"

if os.path.exists(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise FileNotFoundError(f"Unable to load image: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face Detection", img)
    cv2.imwrite("LIST OF EXPERIMENTS/exp33/exp33_output.jpg", img)
    print(f"Faces detected: {len(faces)}")

    cv2.waitKey(0)
else:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Unable to open camera. Add exp33.jpg to use image detection.")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()

cv2.destroyAllWindows()
