import cv2

cap = cv2.VideoCapture('video.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

# Normal speed
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow('Normal Speed', frame)
    if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'): break

# Slow motion
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow('Slow Motion', frame)
    if cv2.waitKey(int(2000/fps)) & 0xFF == ord('q'): break

# Fast motion
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow('Fast Motion', frame)
    if cv2.waitKey(int(500/fps)) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
print("Done!")
