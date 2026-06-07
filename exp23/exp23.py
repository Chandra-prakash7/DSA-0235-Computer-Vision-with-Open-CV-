import cv2
import numpy as np

img = cv2.imread("LIST OF EXPERIMENTS/exp23/exp23.png", 0)

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp23/exp23.png")

kernel = np.array([[-1,-1,-1],
                   [-1,8,-1],
                   [-1,-1,-1]])

boundary = cv2.filter2D(img, -1, kernel)

cv2.imshow("Boundary Detection", boundary)
cv2.imwrite("LIST OF EXPERIMENTS/exp23/exp23_output.png", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
