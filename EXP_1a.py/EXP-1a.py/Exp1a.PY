import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'Picture1a.png')
output_path = os.path.join(script_dir, 'Picture1a_gray.png')

if not os.path.exists(img_path):
    raise FileNotFoundError(f'Image not found: {img_path}')

img = cv2.imread(img_path)
if img is None:
    raise ValueError(f'Failed to load image: {img_path}')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(output_path, gray)
print(f'Converted to grayscale and saved: {output_path}')
