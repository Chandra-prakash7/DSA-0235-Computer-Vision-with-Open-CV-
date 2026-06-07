import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "exp19.png")
img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Unable to load image: {img_path}")

blur = cv2.GaussianBlur(img,(9,9),10)

sharp = cv2.addWeighted(img,1.5,blur,-0.5,0)
output_path = os.path.join(script_dir, "exp19_output.png")
cv2.imwrite(output_path, sharp)
cv2.imshow("Unsharp Masking", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()