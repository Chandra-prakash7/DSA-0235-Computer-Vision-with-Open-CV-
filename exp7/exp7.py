import cv2
import numpy as np

image = cv2.imread('exp7.jpg')
h, w = image.shape[:2]

# Define 3 source points (corners of the image)
pts1 = np.float32([[0, 0], [w-1, 0], [0, h-1]])

# Define 3 destination points (where to transform them)
pts2 = np.float32([[w*0.1, h*0.1], [w*0.9, h*0.2], [w*0.1, h*0.9]])

# Get affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
affine_image = cv2.warpAffine(image, matrix, (w, h))
cv2.imwrite('exp7_affine.jpg', affine_image)

print("Affine transformation completed!")
print("Saved as 'exp7_affine.jpg'")
