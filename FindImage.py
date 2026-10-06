import glob
import cv2


def DisplayImage(imageNumber = 1):
    """Displays and gets a reference to a specific image in the folder "Cropped and perspective corrected boards".
    
    The default is image number 1 
    
    @param imageNumber: int
    @returns: A reference to the specific numbered image in "Cropped and perspective corrected boards"
    """
    if imageNumber in range(len(glob.glob("King Domino dataset\\Cropped and perspective corrected boards\\*.jpg"))) and imageNumber > 0:      
        image = glob.glob(f"King Domino dataset\\Cropped and perspective corrected boards\\{imageNumber}.jpg")
        image = cv2.imread(image[0])
        # Display the image
        cv2.imshow(f"Image number {imageNumber} display", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return image
    else:
        print(f"The number needs to be in range from 1-{len(glob.glob("King Domino dataset\\Cropped and perspective corrected boards\\*.jpg"))}")
    return None

def GetImage(imageNumber = 1):
    """Gets a reference to a specific image in the folder "Cropped and perspective corrected boards".
    
    The default is image number 1 
    
    @param imageNumber: int
    @returns: A reference to the specific numbered image in "Cropped and perspective corrected boards"
    """
    if imageNumber in range(len(glob.glob("King Domino dataset\\Cropped and perspective corrected boards\\*.jpg"))) and imageNumber > 0:      
        image = glob.glob(f"King Domino dataset\\Cropped and perspective corrected boards\\{imageNumber}.jpg")
        image = cv2.imread(image[0])
        return image
    else:
        print(f"The number needs to be in range from 1-{len(glob.glob("King Domino dataset\\Cropped and perspective corrected boards\\*.jpg"))}")
    return None

def GetAllImages():
    """Make a list containing a reference to every image in the folder "Cropped and perspective corrected boards".

    Note: The range of the list is 0-73 (Unless changed), and the images have not been read yet.

    @param None
    @returns: A list containing a reference to every image in the folder "Cropped and perspective corrected boards"
    """
    listOfImages = []
    for images in glob.glob("King Domino dataset\\Cropped and perspective corrected boards\\*.jpg"):
        listOfImages.append(images)
    return listOfImages
