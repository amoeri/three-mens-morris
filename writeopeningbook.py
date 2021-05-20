from game import Board
from minimax import Minimax
import copy

f = open("openings.book", "w")

MAX_DEPTH = 8
minimax = Minimax(None, MAX_DEPTH)
initialBoard = Board()

firstPlayerOpeningBook = {'boad':'move'}
def book(this, board, depth):
  moves = board.legalMoves(1)
  if len(moves) <= 0:
    return
  for move in moves:
    nextBoard = Board(copy.deepcopy(board.board))
    nextBoard.move(move)
    evaluation = minimax.minimax(-1, nextBoard, depth)
    if evaluation == 1:
      this[str(board.board)] = str(move)
      adversaryMoves = nextBoard.legalMoves(-1)
      for adversaryMove in adversaryMoves:
        newBoard = Board(copy.deepcopy(nextBoard.board))
        newBoard.move(adversaryMove)
        book(this, newBoard, depth + 2)
      break

book(firstPlayerOpeningBook, initialBoard, 0)
f.write(str(firstPlayerOpeningBook) + "\n")

def secondBook(this, board, depth):
  moves = board.legalMoves(1)
  if len(moves) <= 0:
    return
  for move in moves:
    nextBoard = Board(copy.deepcopy(board.board))
    nextBoard.move(move)
    evaluation = minimax.minimax(1, nextBoard, depth)
    if evaluation == -1:
      this[str(board.board)] = str(move)
      adversaryMoves = nextBoard.legalMoves(1)
      for adversaryMove in adversaryMoves:
        newBoard = Board(copy.deepcopy(nextBoard.board))
        newBoard.move(adversaryMove)
        book(this, newBoard, depth + 2)
      break

secondPlayerOpeningBook = {'boad':'move'}
for move in initialBoard.legalMoves(1):
  newBoard = Board(copy.deepcopy(initialBoard.move(move)))
  secondBook(secondPlayerOpeningBook, newBoard, 0)
f.write(str(secondPlayerOpeningBook) + "\n")

f.close()
