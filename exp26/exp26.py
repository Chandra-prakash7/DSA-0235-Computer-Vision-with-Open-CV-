import cv2
import numpy as np

img = cv2.imread("LIST OF EXPERIMENTS/exp26/exp26.png", 0)

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp26/exp26.png")

kernel = np.ones((5,5), np.uint8)

opening = cv2.morphologyEx(
    img,
    cv2.MORPH_OPEN,
    kernel)

cv2.imshow("Opening", opening)
cv2.imwrite("LIST OF EXPERIMENTS/exp26/exp26_output.png", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
