import cv2

img = cv2.imread("object.jpg")

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()