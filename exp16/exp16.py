import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "exp16.png")
img = cv2.imread(img_path, 0)

if img is None:
    raise FileNotFoundError(f"Unable to load image: {img_path}")

lap = cv2.Laplacian(img, cv2.CV_64F)

output_path = os.path.join(script_dir, "exp16_output.png")
cv2.imwrite(output_path, lap)

cv2.imshow("Laplacian", lap)

cv2.waitKey(0)
cv2.destroyAllWindows()