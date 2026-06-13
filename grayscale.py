import cv2

img = cv2.imread(r"C:\Users\ADHUNA KAMLE\Desktop\Week2-ComputerVision\object.jpg")

if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()