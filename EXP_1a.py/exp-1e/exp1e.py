import cv2
import numpy as np

# Read image
image = cv2.imread('Exp1e.jpg')

# Create a kernel for erosion
# Larger kernel = more erosion
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Apply erosion
eroded = cv2.erode(image, kernel, iterations=2)

# Save the eroded image
cv2.imwrite('Exp1e_eroded.jpg', eroded)

print("Done! Eroded image saved as 'Exp1e_eroded.jpg'")
