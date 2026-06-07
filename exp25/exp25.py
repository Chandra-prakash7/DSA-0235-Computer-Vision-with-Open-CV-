import cv2
import numpy as np

img = cv2.imread("LIST OF EXPERIMENTS/exp25/exp25.png", 0)

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp25/exp25.png")

kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Dilation", dilation)
cv2.imwrite("LIST OF EXPERIMENTS/exp25/exp25_output.png", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
