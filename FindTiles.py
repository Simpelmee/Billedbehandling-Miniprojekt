import cv2
import numpy as np

image = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Couldnt read miv")
    exit()

#size of picture
h, w = image.shape

GRID_COLS = 5
GRID_ROWS = 5

TILE_W = w // GRID_COLS
TILE_H = h // GRID_ROWS

#list of found tiles
tiles = []

vis = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

#loop through all rows
for y in range(0,h,TILE_H):
    #loop through all cols 
    for x in range(0,w,TILE_W):

        #ROI
        tile = image[y:y+TILE_H, x:x+TILE_W]

        #std measures pixelvalue 
        if tile.std() < 11.6:
            continue

        #the found tiles
        tiles.append((x,y,TILE_W,TILE_H))

        cv2.rectangle(vis, (x,y), (x+TILE_W, y+TILE_H), (0,255,0), 2)

print("tiles found:", len(tiles))

cv2.imshow("Tile borders", vis)
cv2.waitKey(0)
cv2.destroyAllWindows()