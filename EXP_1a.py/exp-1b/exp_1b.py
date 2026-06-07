import cv2

# Read image
image = cv2.imread('Exp1b.jpg')

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# Save blurred image
cv2.imwrite('Exp1b_blurred.jpg', blurred)

print("Done! Blurred image saved as 'Exp1b_blurred.jpg'")
