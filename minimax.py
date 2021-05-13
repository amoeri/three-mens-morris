import copy
import random
from game import Board

class Minimax:

  def __init__(self, id, maxDepth=7):
    self.id = id
    self.name = "Player " + str(id) + " (Minimax)"
    self.maxDepth = maxDepth
  
  def getNextMove(self, player, board):
    move = self.minimax(player, board, 0)[1]
    if move == ():
      moves = board.legalMoves(player)
      move = moves[random.randint(0, len(moves) - 1)]
    return move

  def minimax(self, player, board, depth):
    if board.winner() != 0:
      # print(str(depth) + " Board has winner")
      return (board.winner(), ())
    if depth >= self.maxDepth:
      # print(str(depth) + " Max depth reached")
      return (0, ())
    moves = board.legalMoves(player)
    evaluations = []
    for move in moves:
      nextBoard = copy.deepcopy(board)
      nextBoard.move(move)
      if nextBoard.winner() == player:
        return (player, move)
      evaluations.append((self.minimax(player * -1, nextBoard, depth + 1), move))
    for evaluation in evaluations:
      if evaluation[0] == player:
        # print(str(depth) + " Winning move found: " + str(evaluation[1]))
        return (player, evaluation[1])
    # print(str(depth) + " No winning move found")
    for evaluation in evaluations:
      if evaluation[0] == 0 and evaluation[1] != ():
        # print(str(depth) + "Even move found")
        return (0, evaluation[1])
    for evaluation in evaluations:
      if evaluation[0] == 0:
        # print(str(depth) + "Even move found")
        return (0, ())
    # print(str(depth) + " No nonempty equal move found")
    # print(str(depth) + " Returning losing move")
    return (player * -1, evaluations[0][1])
