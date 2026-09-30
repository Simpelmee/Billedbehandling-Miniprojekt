import FindImage
import cv2

image = FindImage.GetImage()

print(image)

#thresh = cv2.cvtColor(str(image), cv2.THRESH_BINARY)

#img = cv2.imread(image)

cv2.imshow("Binary Threshold", image)
cv2.waitKey(0)
cv2.destroyAllWindows()