import cv2
import numpy as np

img = cv2.imread("LIST OF EXPERIMENTS/exp29/exp29.png", 0)

kernel = np.ones((5,5), np.uint8)

blackhat = cv2.morphologyEx(
    img,
    cv2.MORPH_BLACKHAT,
    kernel)

cv2.imshow("Original", img)
cv2.imshow("Black Hat", blackhat)
cv2.imwrite("LIST OF EXPERIMENTS/exp29/exp29_output.png", blackhat)
    
cv2.waitKey(0)
cv2.destroyAllWindows()