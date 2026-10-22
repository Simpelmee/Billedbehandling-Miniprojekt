#Example of how the board (2D-array), should look like
board = [[("plain", 0), ("water", 0), ("tree", 0), ("tree", 0),("tree", 0)],
         [("plain", 0), ("tree", 0), ("tree", 0), ("tree", 1), ("plain", 0)],
         [("plain", 0), ("ground", 1), ("crown", 0), ("tree", 0), ("plain", 0)],
         [("plain", 0), ("ground", 2), ("water", 0), ("plain", 2), ("plain", 1)],
         [("tree", 0), ("water", 1), ("water", 0), ("plain", 1), ("farm", 0)]
"""
board = [[("farm", 0), ("stone", 0), ("farm", 0), ("space", 2),("stone", 0)],
         [("space", 1), ("stone", 1), ("farm", 0), ("farm", 0), ("tree", 0)],
         [("space", 2), ("stone", 0), ("crown", 0), ("farm", 0), ("farm", 0)],
         [("space", 2), ("space", 3), ("plain", 0), ("plain", 0), ("farm", 1)],
         [("farm", 0), ("farm", 0), ("stone", 0), ("stone", 0), ("plain", 0)]
         ] #score: 43 - image 2 

board =[[("farm", 0), ("farm", 0), ("plain", 0), ("plain", 0),("empty", 0)],
         [("tree", 0), ("water", 1), ("water", 0), ("water", 0), ("empty", 0)],
         [("plain", 0), ("plain", 0), ("plain", 2), ("tree", 0), ("water", 0)],
         [("plain", 0), ("stone", 2), ("plain", 0), ("farm", 0), ("water", 0)],
         [("stone", 0), ("stone", 0), ("crown", 0), ("farm", 0), ("water", 1)]
         ] #score: 22 - image 16
"""
def CheckBurnable(tileType, row, col):
    """This function is used by CalculateScore(), to find the same type of tiles that are connected to eachother

    @param tileType: The type that the tile is, which we use to look for the same type around it
    @param row: Indicating the row in the 2D array, like a matrix so (row, x)
    @param col: Indicating the col in the 2D array, like a matrix so (x, col)
    @returns: A list with the found matches to the given tile type
    """
    burnQueue = []
    if row+1 < len(board[0]):
        if tileType == board[row+1][col][0] and board[row+1][col][0] != "empty":
            burnQueue.append((row+1, col))
    if row-1 >= 0:
        if tileType == board[row-1][col][0] and board[row-1][col][0] != "empty":
            burnQueue.append((row-1, col))
    if col+1 < len(board[1]):
        if tileType == board[row][col+1][0] and board[row][col+1][0] != "empty":
            burnQueue.append((row, col+1))
    if col-1 >= 0:
        if tileType == board[row][col-1][0] and board[row][col-1][0] != "empty":
            burnQueue.append((row, col-1))
    return burnQueue

def CalculateScore(board = board):
    """This function calculates the score on the board, using the grassfire algorithm.
    
    @param board: The board (2D-array) to be calulated, were the element in the board is tuples like ("farm", 1), where the first index of the tuple indicate the tile type, and the second index indicate the amount of crowns on the tile
    @returns: The calculated score for the given board (2D-array of tuples)
    """
    score = 0
    for row in range(len(board[0])):
        for col in range(len(board[1])):
            connectedTiles = 1
            crownScore = 0
            tileType, crownAmount = board[row][col]
            board[row][col] = ("empty", 0)
            crownScore = crownAmount
            burnList = []
            burnList.extend(CheckBurnable(tileType, row, col))
            while len(burnList) > 0:
                hits = burnList[0]
                tileType, crownAmount = board[hits[0]][hits[1]]
                connectedTiles += 1
                crownScore += crownAmount
                board[hits[0]][hits[1]] = ("empty", 0)
                burnList.extend(CheckBurnable(tileType, hits[0], hits[1]))
                burnList = list(dict.fromkeys(burnList))
                burnList.pop(0)

            score += connectedTiles * crownScore

    return score