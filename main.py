import TileTyping
import FindImage
import FindCrowns
import CalculateScore
import FindTiles

board = [[("empty", 0) for col in range(5)] for row in range(5)]

y = 0
x = 0

imageNumber = 36

img = FindImage.GetImage(imageNumber)
tiles, _ = FindTiles.FindTiles(img)

counter = 0

for row in range(5):
    for col in range(5):
        tileType = TileTyping.SquareType(img[tiles[counter][1]: tiles[counter][1]+tiles[counter][3], tiles[counter][0]:tiles[counter][0]+tiles[counter][2]])
        crownAmount = FindCrowns.FindCrown(img[tiles[counter][1]: tiles[counter][1]+tiles[counter][3], tiles[counter][0]:tiles[counter][0]+tiles[counter][2]])[0]

        board[row][col] = (str(tileType), crownAmount)
        counter += 1
#print(board)
print(CalculateScore.CalculateScore(board))
FindCrowns.ShowCrown(img, FindCrowns.FindCrown(img))