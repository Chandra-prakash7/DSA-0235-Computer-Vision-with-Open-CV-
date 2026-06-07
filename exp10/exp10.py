import cv2
import numpy as np

image = cv2.imread('exp10.png')
h, w = image.shape[:2]

# 4 source points (corners)
src_pts = np.float32([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]])

# 4 destination points (homography transformation)
dst_pts = np.float32([[0, h*0.2], [w-1, 0], [w*0.1, h-1], [w-1, h*0.8]])

# Compute homography matrix (3x3)
H, status = cv2.findHomography(src_pts, dst_pts)

# Apply homography transformation
homography_image = cv2.warpPerspective(image, H, (w, h))
cv2.imwrite('exp10_homography.png', homography_image)

print("Homography transformation completed!")
print(f"Homography Matrix:\n{H}")
print("Saved as 'exp10_homography.png'")
