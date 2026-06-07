import cv2

cap = cv2.VideoCapture(0)

# Normal speed
print("Normal Speed - Press 'q' to quit")
while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(33) & 0xFF == ord('q'): break

# Slow motion
print("Slow Motion - Press 'q' to quit")
while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'): break

# Fast motion
print("Fast Motion - Press 'q' to quit")
while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
print("Done!")
