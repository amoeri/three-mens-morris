import ast

class Reader:

  def __init__(self, id, fallbackplayer):
    self.id = id
    self.name = "Player " + str(id) + " (Reader + " + fallbackplayer.name + ")"
    self.fallbackplayer = fallbackplayer
    f = open("openings.book", "r")
    self.openingbook = {}
    self.openingbook["1"] = f.readline()
    self.openingbook["-1"] = f.readline()
  
  def getNextMove(self, player, board):
    book = ast.literal_eval(self.openingbook[str(player)])
    if str(board.board) in book:
      return ast.literal_eval(book[str(board.board)])
    return self.fallbackplayer.getNextMove(player, board)
