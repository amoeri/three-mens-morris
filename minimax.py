import game
class Minimax:

  def __init__(self, id):
    self.id = id
    self.name = "Player " + str(id) + " (Minimax)"
  
  def getNextMove(self, player, board):
    moves = board.legalMoves(player)
    # TODO: Implement minimax
    return moves[0]
