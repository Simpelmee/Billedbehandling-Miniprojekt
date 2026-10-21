import cv2
import numpy as np
import FindImage

from imutils.object_detection import non_max_suppression

def FindCrown(img = FindImage.GetImage(), thresh = 0.51, temp = "Crown_crop2.jpg"):
    """Uses Multi-template matching to find the amount of crowns in a given image, with the given threshold and given template
    
    @param img: The given (read) image to find crowns in
    @param thresh: float. The threshold used in multi-template matching
    @param temp: The image of a crown used to multi-template match, default is "Crown_crop2.jpg"
    @returns: The amount of crowns found in the given image, with the following threshold and template. It also returns a list of the locations where the crowns were found in the image 
    """
    #Use "Crown_crop2.jpg" to NOT get ALL crowns but NO misfires
    #Use "Crown_crop.jpg" to get nearly ALL crowns but SOME misfires
    temp = cv2.imread(temp) 

    # save the image dimensions
    W, H = temp.shape[:2]

    # initialize our list of rectangles
    boxes = list()

    # Converting them to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    temp_gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)


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

    return len(boxes), boxes

def ShowCrown(img = FindImage.GetImage(), CrownLocation = FindCrown(), temp = "Crown_crop2.jpg"):
    """A function used to show where the crowns where found in the SAME image used as FindCrown()

    @param img: The given (read) image to show crowns in
    @param CrownLocation: Gets the locations of the crowns, by calling FindCrown(), with the SAME (read) image used for img
    @param temp: The template used doing the multi-template matching in the FindCrown() function
    """
    boxes = CrownLocation[1]

    temp = cv2.imread("Crown_crop2.jpg") 

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


#Showcase of how to we could use this
#imgNumber = 56
#image = FindImage.GetImage(imgNumber)
#print(FindCrown(image)[0])
#ShowCrown(image, FindCrown(image))