import cv2
import numpy as np

img = cv2.imread("LIST OF EXPERIMENTS/exp28/exp28.png", 0)

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp28/exp28.png")

kernel = np.ones((5,5), np.uint8)

gradient = cv2.morphologyEx(
    img,
    cv2.MORPH_GRADIENT,
    kernel)

cv2.imshow("Morphological Gradient", gradient)
cv2.imwrite("LIST OF EXPERIMENTS/exp28/exp28_output.png", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
