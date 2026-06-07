import cv2
import numpy as np

image = cv2.imread('exp6.jpg')
h, w = image.shape[:2]

# Move right
moved_right = cv2.warpAffine(image, np.float32([[1, 0, 100], [0, 1, 0]]), (w, h))
cv2.imwrite('exp6_moved_right.jpg', moved_right)

# Move down
moved_down = cv2.warpAffine(image, np.float32([[1, 0, 0], [0, 1, 100]]), (w, h))
cv2.imwrite('exp6_moved_down.jpg', moved_down)

print("Done! Images moved and saved.")
