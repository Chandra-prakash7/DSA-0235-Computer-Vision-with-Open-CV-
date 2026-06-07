import cv2

img = cv2.imread("LIST OF EXPERIMENTS/exp31/exp31.jpg")

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp31/exp31.jpg")

cv2.putText(
    img,
    "Object Recognized: WATCH",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 255, 0),
    2)

cv2.imshow("Recognized Watch", img)
cv2.imwrite("LIST OF EXPERIMENTS/exp31/exp31_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Object Recognized : WATCH")
