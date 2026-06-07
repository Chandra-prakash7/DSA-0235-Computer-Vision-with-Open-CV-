import cv2

# Read image
image = cv2.imread('Exp1c.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
# Parameters: (image, threshold1, threshold2)
edges = cv2.Canny(gray, 100, 200)

# Save the edge-detected image
cv2.imwrite('Exp1c_outline.jpg', edges)

print("Done! Outline image saved as 'Exp1c_outline.jpg'")
