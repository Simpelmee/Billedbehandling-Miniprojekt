import cv2
import numpy as np
import FindImage

def FindBlue(img):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define the lower and upper bounds for the blue color in HSV
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    # Create a mask that captures only the blue color in the image
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Return the mask for further processing or display
    return mask

def FindYellow(img):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define the lower and upper bounds for the yellow color in HSV
    lower_yellow = np.array([20, 230, 100])
    upper_yellow = np.array([30, 255, 255])

    # Create a mask that captures only the yellow color in the image
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Return the mask for further processing or display
    return mask

def FindLightGreen(img):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define the lower and upper bounds for the green color in HSV
    lower_green = np.array([30, 50, 100])
    upper_green = np.array([80, 255, 255])

    # Create a mask that captures only the green color in the image
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Return the mask for further processing or display
    return mask

def FindDarkGreen(img):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define the lower and upper bounds for the dark green color in HSV
    lower_dark_green = np.array([40, 0, 0])
    upper_dark_green = np.array([80, 255, 100])

    # Create a mask that captures only the dark green color in the image
    mask = cv2.inRange(hsv, lower_dark_green, upper_dark_green)

    # Return the mask for further processing or display
    return mask

def FindBeige(img):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define the lower and upper bounds for the beige color in HSV
    lower_beige = np.array([5, 0, 80])
    upper_beige = np.array([30, 230, 150])

    # Create a mask that captures only the beige color in the image
    mask = cv2.inRange(hsv, lower_beige, upper_beige)

    # Return the mask for further processing or display
    return mask

def FindBlack(img):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define the lower and upper bounds for the black color in HSV
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 100, 30])

    # Create a mask that captures only the black color in the image
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Return the mask for further processing or display
    return mask
