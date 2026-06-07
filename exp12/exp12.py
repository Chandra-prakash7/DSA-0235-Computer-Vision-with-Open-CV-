import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "exp12.png")
img = cv2.imread(img_path, 0)

edges = cv2.Canny(img,100,200)

output_path = os.path.join(script_dir, "exp12_output.png")
cv2.imwrite(output_path, edges)

cv2.imshow("Canny Edge", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()