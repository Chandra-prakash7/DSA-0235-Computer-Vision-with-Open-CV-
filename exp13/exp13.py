import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "exp13.png")
img = cv2.imread(img_path, 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

output_path = os.path.join(script_dir, "exp13_output.png")
cv2.imwrite(output_path, sobelx)

cv2.imshow("Sobel X", sobelx)

cv2.waitKey(0)
cv2.destroyAllWindows()