import cv2
import numpy as np
import FindImage

from imutils.object_detection import non_max_suppression



# Reading the image and the template
img = FindImage.GetImage(53)

#Use "Crown_crop2.jpg" to NOT get ALL crowns but NO misfires
#Use "Crown_crop.jpg" to get nearly ALL crowns but SOME misfires
temp = cv2.imread("Crown_crop2.jpg") 

cv2.imshow("Img", img)

# save the image dimensions
W, H = temp.shape[:2]

# Define a minimum threshold
thresh = 0.51 #0.51

# initialize our list of rectangles
boxes = list()

# Converting them to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

temp_gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", img_gray)


for i in range(4):
    # Passing the image to matchTemplate method
    match = cv2.matchTemplate(image=img_gray, templ=temp_gray, method=cv2.TM_CCOEFF_NORMED)

    # Select rectangles with
    # confidence greater than threshold
    (y_points, x_points) = np.where(match >= thresh)

    # loop over the starting (x, y)-coordinates again
    for (x, y) in zip(x_points, y_points):
    
        # update our list of rectangles
        boxes.append((x, y, x + W, y + H))

    temp_gray = cv2.rotate(temp_gray, cv2.ROTATE_90_CLOCKWISE)


# apply non-maxima suppression to the rectangles
# this will create a single bounding box
boxes = non_max_suppression(np.array(boxes))

# loop over the final bounding boxes
for (x1, y1, x2, y2) in boxes:
  
    # draw the bounding box on the image
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3) #Uses BGR instead of RGB

# Show the template and the final output
cv2.imshow("Template", temp)
cv2.imshow("After NMS", img)
cv2.waitKey(0)

# destroy all the windows 
# manually to be on the safe side
cv2.destroyAllWindows()