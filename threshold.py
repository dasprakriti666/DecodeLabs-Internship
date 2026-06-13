import cv2

img = cv2.imread(r"C:\Users\ADHUNA KAMLE\Desktop\Week2-ComputerVision\object.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)

_, thresh = cv2.threshold(
    blur,
    127,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Gray", gray)
cv2.imshow("Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()