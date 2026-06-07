import cv2
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "exp18.png")
img = cv2.imread(img_path, 0)

if img is None:
    raise FileNotFoundError(f"Unable to load image: {img_path}")

kernel = np.array([[-1,-1,-1],
                   [-1,8,-1],
                   [-1,-1,-1]])

output = cv2.filter2D(img,-1,kernel)

output_path = os.path.join(script_dir, "exp18_output.png")
cv2.imwrite(output_path, output)

cv2.imshow("Sharpened", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
