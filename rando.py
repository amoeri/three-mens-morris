import random

class Rando:

  def __init__(self, id):
    self.id = id
    self.name = "Player " + str(id) + " (Random)"
  
  def getNextMove(self, player, board):
    moves = board.legalMoves(player)

    return moves[random.randint(0, len(moves) - 1)]
