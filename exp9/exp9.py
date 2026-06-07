import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

if not cap.isOpened():
    print("Error: Cannot load video file!")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('video_perspective.avi', fourcc, fps, (w, h))

# Perspective transformation points
pts1 = np.float32([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]])
pts2 = np.float32([[0, 0], [w-1, h*0.3], [w*0.2, h-1], [w-1, h-1]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret: break
    
    perspective_frame = cv2.warpPerspective(frame, matrix, (w, h))
    out.write(perspective_frame)
    frame_count += 1

cap.release()
out.release()
print(f"Done! Processed {frame_count} frames")
print(f"Saved as 'video_perspective.avi'")
