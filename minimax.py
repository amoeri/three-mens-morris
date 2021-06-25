import copy
import random
from game import Board
from functools import cache

class Minimax:

  def __init__(self, id, maxDepth=7):
    self.id = id
    self.name = "Player " + str(id) + " (Minimax, depth: " + str(maxDepth) + ")"
    self.maxDepth = maxDepth
  
  def getNextMove(self, player, board):
    moves = board.legalMoves(player)
    zeroMoves = []
    for move in moves:
      nextBoard = Board(copy.deepcopy(board.board))
      nextBoard.move(move)
      evaluation = self.minimax(player * -1, nextBoard, 0)
      if evaluation == player:
        return move
      if evaluation == 0:
        zeroMoves.append(move)
    if len(zeroMoves) > 0:
      return zeroMoves[random.randint(0, len(zeroMoves) - 1)]
    return moves[random.randint(0, len(moves) - 1)]

  @cache
  def minimax(self, player, board, depth):
    if board.winner() != 0:
      return board.winner()
    
    if depth >= self.maxDepth:
      return 0
  
    evaluations = []
    moves = board.legalMoves(player)
    for move in moves:
      nextBoard = Board(copy.deepcopy(board.board))
      nextBoard.move(move)
      evaluations.append(self.minimax(player * -1, nextBoard, depth + 1))

    if player == 1:
      return max(evaluations)
    return min(evaluations)
