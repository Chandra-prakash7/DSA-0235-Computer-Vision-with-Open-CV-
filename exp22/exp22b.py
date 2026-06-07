import cv2

img = cv2.imread("LIST OF EXPERIMENTS/exp22/exp22.png")

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp22/exp22.png")

crop = img[50:120, 50:120]

img[80:150, 180:250] = crop

cv2.imshow("Output", img)
cv2.imwrite("LIST OF EXPERIMENTS/exp22/exp22b_output.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
