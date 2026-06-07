import cv2
import numpy as np

img = cv2.imread("LIST OF EXPERIMENTS/exp27/exp27.png", 0)

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp27/exp27.png")

kernel = np.ones((5,5), np.uint8)

closing = cv2.morphologyEx(
    img,
    cv2.MORPH_CLOSE,
    kernel)

cv2.imshow("Closing", closing)
cv2.imwrite("LIST OF EXPERIMENTS/exp27/exp27_output.png", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
