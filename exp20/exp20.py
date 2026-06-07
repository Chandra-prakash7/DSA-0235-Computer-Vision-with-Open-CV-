import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "exp20.png")
img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Unable to load image: {img_path}")

blur = cv2.GaussianBlur(img,(5,5),0)

highboost = cv2.addWeighted(img,2.0,blur,-1.0,0)

output_path = os.path.join(script_dir, "exp20_output.png")
cv2.imwrite(output_path, highboost)

cv2.imshow("High Boost", highboost)

cv2.waitKey(0)
cv2.destroyAllWindows()
