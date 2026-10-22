import cv2
import FindColour
import TileTyping

def TerrainGrid(img):
    rows = 5
    cols = 5

    height, width = img.shape[:2]

    square_height = height // rows
    square_width = width // cols

    terrain_grid = []

    # Loop through each square in the grid and classify its terrain type
    for row in range(rows):
        # Create a list to hold the terrain types for the current row
        terrain_row = []
        for col in range(cols):
            x1 = col * square_width
            x2 = (col + 1) * square_width

            y1 = row * square_height
            y2 = (row + 1) * square_height

            square = img[y1:y2, x1:x2]

            # Get the terrain type for the square
            terrain_type = TileTyping.SquareType(square)
            # Put the terrain type in the terrain row
            terrain_row.append(terrain_type)
        # Put the terrain row in the terrain grid
        terrain_grid.append(terrain_row)

    return terrain_grid

#list = TerrainGrid(img)

#print("Terrain Grid:", list)