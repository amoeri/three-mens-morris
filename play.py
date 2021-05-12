from game import Game, Board

from human import Human

# board = Board()
# board.move((1, (0, 0)))
# board.move((1, (0, 1)))
# board.move((1, (0, 2)))
# board.move(((0, 0), (1, 0)))
# print(board.legalDestinations((1, 0)))
# print(board.legalDestinations((0, 0)))
# print(board.legalMoves(1))
# print(board)
# print(board.winner())

# board.move(((1, 0), (0, 0)))
# print(board)
# print(board.winner())

# human = Human()

# print(str(human.getNextMove(1, board)))

import sys

p = []

n = len(sys.argv)

for i in range(1, 3):
  if sys.argv[i] == "human":
    p.append(Human(i - 1))

games = 1
if n == 4:
  games = int(sys.argv[3])

print("Starting " + str(games) + " game(s) between " + p[0].name + " and " + p[1].name)

wins = [0, 0]
for gamenr in range(games):
  print("Starting game #" + str(gamenr))
  if (gamenr % 2) == 0:
    game = Game(p[0], p[1])
  else:
    game = Game(p[1], p[0])
  winner = game.start()
  wins[winner.id] += 1
  print("And the winner of game #" + str(gamenr) +" is Player " + str(winner.name))

if games > 1:
  print("The series of " + str(games) + " games is over.")
  print(p[0].name + " has won " + str(wins[0]) + " time(s) and " + p[1].name + ") has won " + str(wins[1]) + " time(s)")
  if wins[0] > wins[1]:
    print("Congratulations to " + p[0].name + "!!!")
  elif wins[1] > wins[0]:
    print("Congratulations to " + p[1].name + "!!!")
  else:
    print("Congratulations to both player for this draw...")
