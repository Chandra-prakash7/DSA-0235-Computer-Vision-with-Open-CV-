import cv2

img = cv2.imread("LIST OF EXPERIMENTS/exp35/exp35.jpg")

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp35/exp35.jpg")

x1, y1 = 180, 80
x2, y2 = 430, 330

obj = img[y1:y2, x1:x2]

cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow("Rectangle", img)
cv2.imshow("Extracted Object", obj)

cv2.imwrite("LIST OF EXPERIMENTS/exp35/exp35_rectangle.jpg", img)
cv2.imwrite("LIST OF EXPERIMENTS/exp35/exp35_extracted.jpg", obj)

cv2.waitKey(0)
cv2.destroyAllWindows()
