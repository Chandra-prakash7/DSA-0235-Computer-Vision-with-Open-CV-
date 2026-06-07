import cv2
import numpy as np

img = cv2.imread("LIST OF EXPERIMENTS/exp29/exp29.png", 0)

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp29/exp29.png")

kernel = np.ones((5,5), np.uint8)

tophat = cv2.morphologyEx(
    img,
    cv2.MORPH_TOPHAT,
    kernel)

cv2.imshow("Original", img)
cv2.imshow("Top Hat", tophat)
cv2.imwrite("LIST OF EXPERIMENTS/exp29/exp29_output.png", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
