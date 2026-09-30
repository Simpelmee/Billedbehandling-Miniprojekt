import glob
import cv2


def DisplayImage():
    #Replace "King Domino dataset\\Cropped and perspective corrected boards\\1.jpg" with King Domino dataset\\Cropped and perspective corrected boards\\*.jpg
    #To get all images
    for images in glob.glob("King Domino dataset\\Cropped and perspective corrected boards\\1.jpg"):
        image = images

    picture = cv2.imread(image)

    # Display the image
    cv2.imshow('image', picture)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return image

def GetImage():
        #Replace "King Domino dataset\\Cropped and perspective corrected boards\\1.jpg" with King Domino dataset\\Cropped and perspective corrected boards\\*.jpg
    #To get all images
    for images in glob.glob("King Domino dataset\\Cropped and perspective corrected boards\\1.jpg"):
        image = images
        image = cv2.imread(image)
    return image