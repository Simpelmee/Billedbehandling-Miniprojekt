import cv2

img = cv2.imread('Crown_Ref.jpg')

print(type(img))

# Shape of the image
print("Shape of the image", img.shape)

# [rows, columns] 
crop = img[6:25, 5:28]  

cv2.imwrite("Crown_crop3.jpg", crop)

cv2.imshow('original', img)
cv2.imshow('cropped', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Hello, World!")