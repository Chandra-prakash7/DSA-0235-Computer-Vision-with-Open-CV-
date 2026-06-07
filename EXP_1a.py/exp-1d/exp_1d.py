import cv2
import numpy as np

# Read image
image = cv2.imread('Exp1d.jpg')

# Create a kernel for dilation
# Larger kernel = more dilation
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Apply dilation
dilated = cv2.dilate(image, kernel, iterations=2)

# Save the dilated image
cv2.imwrite('Exp1d_dilated.jpg', dilated)

print("Done! Dilated image saved as 'Exp1d_dilated.jpg'")
