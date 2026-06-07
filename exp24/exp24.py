import cv2
import numpy as np

img = cv2.imread("LIST OF EXPERIMENTS/exp24/exp24.png", 0)

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp24/exp24.png")

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Erosion", erosion)
cv2.imwrite("LIST OF EXPERIMENTS/exp24/exp24_output.png", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
