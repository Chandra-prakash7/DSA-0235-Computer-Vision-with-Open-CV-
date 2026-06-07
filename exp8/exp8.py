import cv2
import numpy as np

image = cv2.imread('exp8.png')
h, w = image.shape[:2]

# 4 source points (corners)
pts1 = np.float32([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]])

# 4 destination points
pts2 = np.float32([[0, 0], [w-1, h*0.3], [w*0.2, h-1], [w-1, h-1]])

# Get perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
perspective_image = cv2.warpPerspective(image, matrix, (w, h))
cv2.imwrite('exp8_perspective.png', perspective_image)

print("Perspective transformation completed!")
print("Saved as 'exp8_perspective.png'")
