def tochar(value):
  match value:
    case 1:
      return "○"
    case -1:
      return "●"
    case _:
      return " " #◌

def possibleDestinations(position):
  match position:
    case (0, 0):
      return [(0, 1), (1, 0), (1, 1)]
    case (0, 1):
      return [(0, 0), (0, 2), (1, 1)]
    case (0, 2):
      return [(0, 1), (1, 2), (1, 1)]
    case (1, 0):
      return [(0, 0), (1, 1), (2, 0)]
    case (1, 1):
      return [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    case (1, 2):
      return [(0, 2), (1, 1), (2, 2)]
    case (2, 0):
      return [(1, 0), (2, 1), (1, 1)]
    case (2, 1):
      return [(2, 0), (1, 1), (2, 2)]
    case (2, 2):
      return [(2, 1), (1, 2), (1, 1)]
    case _:
      return []

class Board:
  

  lines = [\
    ((0, 0), (0, 1), (0, 2)),\
    ((1, 0), (1, 1), (1, 2)),\
    ((2, 0), (2, 1), (2, 2)),\
    ((0, 0), (1, 0), (2, 0)),\
    ((0, 1), (1, 1), (2, 1)),\
    ((0, 2), (1, 2), (2, 2)),\
    ((0, 0), (1, 1), (2, 2)),\
    ((0, 2), (1, 1), (2, 0))\
  ]

  def __init__(self):
    self.board = [[0,0,0], [0,0,0], [0,0,0]]

  def __str__(self):
    return tochar(self.board[0][0]) + "───" + tochar(self.board[0][1]) + "───" + tochar(self.board[0][2]) + "\n" \
         + "│ ╲ │ ╱ │\n" \
         + tochar(self.board[1][0]) + "───" + tochar(self.board[1][1]) + "───" + tochar(self.board[1][2]) + "\n" \
         + "│ ╱ │ ╲ │\n" \
         + tochar(self.board[2][0]) + "───" + tochar(self.board[2][1]) + "───" + tochar(self.board[2][2])

  def move(self, move):
    match move:
      case ((x1, y1), (x2, y2)):
        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = 0
      case (p, (x, y)):
        self.board[x][y] = p
   
  def legalDestinations(self, position):
    return list(filter(lambda p: (self.board[p[0]][p[1]] == 0), possibleDestinations(position)))
  
  def hasAllStonesSet(self, player):
    stoneCount = 0
    for x in range(3):
      for y in range(3):
        if self.board[x][y] == player:
          stoneCount += 1
    if stoneCount == 3:
      return True
    return False

  def emptyFields(self):
    fields = []
    for x in range(3):
      for y in range(3):
        if self.board[x][y] == 0:
          fields.append((x, y))
    return fields

  def stonePositions(self, player):
    positions = []
    for x in range(3):
      for y in range(3):
        if self.board[x][y] == player:
          positions.append((x, y))
    return positions

  def legalMoves(self, player):
    moves = []
    if self.hasAllStonesSet(player):
      for position in self.stonePositions(player):
        for destination in self.legalDestinations(position):
          moves.append((position, destination))
    else:
      for field in self.emptyFields():
        moves.append((player, field))
    return moves

  def sumLine(self, line):
    sum = 0
    for position in line:
      sum += self.board[position[0]][position[1]]
    return sum

  def winner(self):
    for line in self.lines:
      if self.sumLine(line) == 3:
        return 1
      elif self.sumLine(line) == -3:
        return -1
    return 0

class Game:
  def __init__(self, player1, player2):
    self.player = []
    self.player.append(player2)
    self.player.append(player1)
    self.board = Board()
    
  def start(self):
    turn = 1 # refers to player1 from the game constructor and will be referred to as 1 on the board
    # thus player to will play on turn 0 and be -1 on the board... confusing, i know
    while self.board.winner() == 0:
      playerid = turn
      if playerid == 0:
        playerid = -1

      self.board.move(self.player[turn].getNextMove(playerid, self.board))

      if turn == 0:
        turn = 1
      else:
        turn = 0
    if self.board.winner() == 1:
      return self.player[1]
    elif self.board.winner() == -1:
      return self.player[0]
    else:
      raise Exception("winner undefined")






