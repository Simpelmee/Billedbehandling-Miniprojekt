import cv2
import FindColour
import FindImage

img = FindImage.GetImage()

def SquareType(square):
    # Find the color masks for the square
    blue = cv2.countNonZero(FindColour.FindBlue(square))
    yellow = cv2.countNonZero(FindColour.FindYellow(square))
    light_green = cv2.countNonZero(FindColour.FindLightGreen(square))
    dark_green = cv2.countNonZero(FindColour.FindDarkGreen(square))
    beige = cv2.countNonZero(FindColour.FindBeige(square))
    black = cv2.countNonZero(FindColour.FindBlack(square))
    red = cv2.countNonZero(FindColour.FindRed(square))

    # Count the number of pixels in each mask
    colours = {
        "blue": blue,
        "yellow": yellow,
        "light_green": light_green,
        "dark_green": dark_green,
        "beige": beige,
        "black": black,
        "red": red
    }
    # Find most common colour
    type = max(colours, key=colours.get)

    # Calculate the total number of pixels in the square
    total_pixels = square.shape[0] * square.shape[1]

    # Only check beige tiles for startTile
    if type == "beige":

        #Calculate percentage of each colour in the square
        red_percentage = red / total_pixels
        blue_percentage = blue / total_pixels
        yellow_percentage = yellow / total_pixels
        dark_green_percentage = dark_green / total_pixels

        # Check if any of those colours are above 15%, if so it is a startTile
        if red_percentage > 0.15 or blue_percentage > 0.15 or yellow_percentage > 0.15 or dark_green_percentage > 0.15:
            return "startTile"
        else:
            return "beige"
        
    return type