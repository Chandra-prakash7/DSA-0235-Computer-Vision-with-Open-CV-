import cv2

# Read image
image = cv2.imread('exp5.jpg')

# Get image dimensions
height, width = image.shape[:2]
center = (width // 2, height // 2)

# Rotate 90 degrees clockwise
matrix_cw = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated_cw = cv2.warpAffine(image, matrix_cw, (width, height))
cv2.imwrite('exp5_clockwise.jpg', rotated_cw)
print("Clockwise rotation (90°) - Saved as 'exp5_clockwise.jpg'")

# Rotate 90 degrees counter-clockwise
matrix_ccw = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_ccw = cv2.warpAffine(image, matrix_ccw, (width, height))
cv2.imwrite('exp5_counter_clockwise.jpg', rotated_ccw)
print("Counter-clockwise rotation (90°) - Saved as 'exp5_counter_clockwise.jpg'")

# Rotate 180 degrees
matrix_180 = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated_180 = cv2.warpAffine(image, matrix_180, (width, height))
cv2.imwrite('exp5_180.jpg', rotated_180)
print("180° rotation - Saved as 'exp5_180.jpg'")

print("Done!")
