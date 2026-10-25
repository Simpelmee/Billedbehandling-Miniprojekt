import cv2
import numpy as np
import FindImage
from FindColour import FindBlue, FindYellow, FindLightGreen, FindDarkGreen, FindBeige, FindBlack

def TileColour(tile_bgr):
    #list of colourmasks
    masks = [
        FindBlue(tile_bgr),
        FindYellow(tile_bgr),
        FindLightGreen(tile_bgr),
        FindDarkGreen(tile_bgr),
        FindBeige(tile_bgr),
        FindBlack(tile_bgr)
    ]

    #goes through every mask - check if there is enough colourpixels
    for mask in masks:
        if cv2.countNonZero(mask) > 50:
            return True
    return False

#makes a grid of tiles and finds the matching pixels   
def FindTiles(imageNumber, grid_cols=5, grid_rows=5):
    image = FindImage.GetImage(25)

    if image is None:
        print("Couldnt read")
        return [], None

    #size of picture
    h, w = image.shape[:2]

    #size of tile based on the grid
    tile_w = w // grid_cols
    tile_h = h // grid_rows

    #list of found tiles
    tiles = []
 
    vis = image.copy()

    #loop through all rows

    for y in range(0,h,tile_h):
        for x in range(0,w,tile_w):
            tile_bgr = image[y:y+tile_h, x:x+tile_w]

            if not TileColour(tile_bgr):
                continue

            #the found tiles
            tiles.append((x,y,tile_w,tile_h))
            cv2.rectangle(vis, (x,y), (x+tile_w, y+tile_h), (0,255,0), 2)

    return tiles,vis

tiles, vis = FindTiles(1)
print("tiles found:", len(tiles))

cv2.imshow("Tile borders", vis)
cv2.waitKey(0)
cv2.destroyAllWindows()