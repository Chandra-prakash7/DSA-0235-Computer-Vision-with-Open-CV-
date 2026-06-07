import cv2

video_path = "LIST OF EXPERIMENTS/exp32/exp32.mp4"
output_path = "LIST OF EXPERIMENTS/exp32/exp32_reversed.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise FileNotFoundError(f"Unable to open video: {video_path}")

frames = []
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

if not frames:
    raise ValueError("No frames found in the video.")

if fps <= 0:
    fps = 30

out = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height))

for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)
    out.write(frame)

    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord("q"):
        break

out.release()
cv2.destroyAllWindows()
