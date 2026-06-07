import cv2

img = cv2.imread("LIST OF EXPERIMENTS/exp22/exp22.png")

if img is None:
    raise FileNotFoundError("Unable to load image: LIST OF EXPERIMENTS/exp22/exp22.png")

cv2.putText(img,
            "Copyright",
            (50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,255,255),
            2)

cv2.imshow("Watermarked Image", img)
cv2.imwrite("LIST OF EXPERIMENTS/exp22/exp22_output.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
