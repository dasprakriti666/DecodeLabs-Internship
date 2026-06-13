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

for cnt in contours:

    area = cv2.contourArea(cnt)

    if area > 1000:

        x, y, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

cv2.imshow("Bounding Box", img)

cv2.waitKey(0)
cv2.destroyAllWindows()