import FindImage
import cv2

image = FindImage.GetImage()

img = cv2.imread(image)

ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", bw_img)
