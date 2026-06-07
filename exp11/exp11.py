import cv2
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "exp11.png")
img = cv2.imread(img_path)

if img is None:
    print("Error: Could not load image.jpg. Please ensure the image file exists in the script directory.")
    exit()

pts1 = np.float32([[0,0],[300,0],[0,300],[300,300]])
pts2 = np.float32([[20,40],[280,20],[40,260],[300,280]])

M = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, M, (350,350))

# Save the result
cv2.imwrite("exp11_output.png", result)
print("✓ Perspective transformation completed successfully!")
print("✓ Output saved as 'exp11_output.png'")