import cv2
import numpy as np
import FindImage
from FindColour import FindBlue, FindYellow, FindLightGreen, FindDarkGreen, FindBeige, FindBlack

def TileColour(tile_bgr):
    masks = [
        FindBlue(tile_bgr),
        FindYellow(tile_bgr),
        FindLightGreen(tile_bgr),
        FindDarkGreen(tile_bgr),
        FindBeige(tile_bgr),
        FindBlack(tile_bgr)
    ]

    for mask in masks:
        if cv2.countNonZero(mask) > 50:
            return True
    return False

def FindTiles(image=FindImage.GetImage(1), grid_cols=5, grid_rows=5):
    if image is None:
        print("Couldnt read")
        return [], None

    #size of picture
    h, w = image.shape[:2]

    TILE_W = w // grid_cols
    TILE_H = h // grid_rows

    #list of found tiles
    tiles = []

    vis = image.copy()

    #loop through all rows
    for y in range(0,h,TILE_H):
            for x in range(0,w,TILE_W):
                tile_bgr = image[y:y+TILE_H, x:x+TILE_W]

                if not TileColour(tile_bgr):
                    continue

                #the found tiles
                tiles.append((x,y,TILE_W,TILE_H))
                cv2.rectangle(vis, (x,y), (x+TILE_W, y+TILE_H), (0,255,0), 2)

    return tiles,vis

#tiles, vis = FindTiles(1)
#print("tiles found:", len(tiles))

#cv2.imshow("Tile borders", vis)
#cv2.waitKey(0)
#cv2.destroyAllWindows()