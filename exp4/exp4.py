import cv2

# Read image from exp-1e directory
image = cv2.imread('../exp-1e/Exp1e.jpg')

# Get original dimensions
height, width = image.shape[:2]
print(f"Original Size: {width}x{height}")

# Scale to bigger size (2x larger)
bigger = cv2.resize(image, (width * 2, height * 2))
cv2.imwrite('Exp1e_bigger.jpg', bigger)
print(f"Bigger Size: {width * 2}x{height * 2} - Saved as 'Exp1e_bigger.jpg'")

# Scale to smaller size (0.5x smaller)
smaller = cv2.resize(image, (width // 2, height // 2))
cv2.imwrite('Exp1e_smaller.jpg', smaller)
print(f"Smaller Size: {width // 2}x{height // 2} - Saved as 'Exp1e_smaller.jpg'")

print("Done!")
