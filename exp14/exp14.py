import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "exp14.png")
img = cv2.imread(img_path, 0)

if img is None:
    raise FileNotFoundError(f"Unable to load image: {img_path}")

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

output_path = os.path.join(script_dir, "exp14_output.png")
cv2.imwrite(output_path, sobely)

cv2.imshow("Sobel Y", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
