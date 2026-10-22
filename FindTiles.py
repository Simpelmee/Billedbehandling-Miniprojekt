import cv2
import numpy as np
import FindImage
from FindColours import Find

def is_tile(tile_bgr):
    masks = [
        FindBlue(tile_bgr),
    ]

    for mask in masks:
        if cv2.countNonZero(mask) > 50:
            return True
    return False

def FindTiles(imageNumber=1, grid_cols=5, grid_rows=5):
    image = FindImage.GetImage(1)

    if image is None:
        print("Couldnt read miv")
        return [], None

    #size of picture
    h, w = image.shape[:2]

    tile_w = w // grid_cols
    tile_h = h // grid_rows

    #list of found tiles
    tiles = []

    vis = image.copy()

    #loop through all rows
    for row in range(grid_rows):
            for col in range(grid_cols):
                x = col * tile_w
                y = row * tile_h

                tile_bgr = image[y:y+tile_h, x:x+tile_w]

                if not is_tile(tile_bgr):
                    continue

            #the found tiles
            tiles.append((x,y,tile_w,tile_h))

            cv2.rectangle(vis, (x,y), (x+TILE_W, y+TILE_H), (0,255,0), 2)

    return tiles,vis

tiles, vis = detect_tiles("picture.jpg")
print("tiles found:", len(tiles))

cv2.imshow("Tile borders", vis)
cv2.waitKey(0)
cv2.destroyAllWindows()