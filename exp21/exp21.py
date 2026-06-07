import cv2

img = cv2.imread("LIST OF EXPERIMENTS/exp21/exp21.png", 0)

equalized = cv2.equalizeHist(img)

cv2.imwrite("LIST OF EXPERIMENTS/exp21/exp21_output.png", equalized)

cv2.imshow("Original", img)
cv2.imshow("Equalized", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
