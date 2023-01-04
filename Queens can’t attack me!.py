def calcLeftOverSpots(board):
  count = 0
  for stripe in board:
    for box in stripe:
      if(box == "X"):
        count+=1
  return count


def fillStraight(board, row, col):
  for i in range(len(board[row])):
    board[row][i] = board[row][i].replace("X", "O")
  for i in range(len(board)):
    board[i][col] = board[i][col].replace("X", "O")

def rightBelow(board, row, col):
  y, x = row, col
  while(y<len(board) and x>=0):
    board[y][x] = board[y][x].replace("X", "O")
    y+=1
    x-=1

def leftBelow(board, row, col):
  y, x = row, col
  while(y<len(board) and x<len(board[0])):
    board[y][x] = board[y][x].replace("X", "O")
    y+=1
    x+=1

def fillDiagonally(board, row, col):
  if(row <= len(board[0])-col+1):
    rightBelow(board, 0, col+row-2)
  else:
    rightBelow(board, row-(len(board[0])-col)-1, len(board[0])-1)
  
  

  if(row <= col):
    leftBelow(board, 0, col-row)
  else:
    leftBelow(board, row-col, 0)


def prettyPrint(board):
  for row in board:
    for i in row:
      print(i, end="")
    print("\n")

n, m = input().split(" ")
n = int(n)
m = int(m)
board = [["X" for j in range(n)] for i in range(n)]

for val in range(m):
  x, y = input().split(" ")
  x = int(x)
  y = int(y)
  board[x-1][y-1] = board[x-1][y-1].replace("X", "Q")
  
  fillStraight(board, x-1, y-1)
  fillDiagonally(board, x, y)


print(calcLeftOverSpots(board))
