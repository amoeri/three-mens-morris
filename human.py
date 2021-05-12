import game
class Human:

  def __init__(self, id):
    self.id = id
    self.name = "Player " + str(id) + " (Human)"
  
  def getNextMove(self, player, board):
    print("It's your turn " + self.name + " (playing with " + game.tochar(player) + ") ! Choose wisely...")
    print(board)
    moves = board.legalMoves(player)
    selection = -1
    while selection not in range(len(moves)):
      print("Your possible moves are:")
      moves = board.legalMoves(player)
      for move, id in zip(moves, range(len(moves))):
        print(str(id) + ": " + str(move))
      selection = int(input())
    return moves[selection]
