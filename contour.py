import cv2

img = cv2.imread("coin.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)

_, thresh = cv2.threshold(
    blur,
    127,
    255,
    cv2.THRESH_BINARY_INV
)

contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

print("Contours Found:", len(contours))

cv2.imshow("Threshold", thresh)
cv2.imshow("Contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()