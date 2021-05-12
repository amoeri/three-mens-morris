from random import Random
from game import Game

from human import Human
from minimax import Minimax
from rando import Rando

import sys

p = []

n = len(sys.argv)

for i in range(1, 3):
  match sys.argv[i]:
    case "human":
      p.append(Human(i - 1))
    case "random":
      p.append(Rando(i - 1))
    case "minimax":
      p.append(Minimax(i - 1))

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
  print("And the winner of game #" + str(gamenr) +" is " + str(winner.name))

if games > 1:
  print("The series of " + str(games) + " games is over.")
  print(p[0].name + " has won " + str(wins[0]) + " time(s) and " + p[1].name + ") has won " + str(wins[1]) + " time(s)")
  if wins[0] > wins[1]:
    print("Congratulations to " + p[0].name + "!!!")
  elif wins[1] > wins[0]:
    print("Congratulations to " + p[1].name + "!!!")
  else:
    print("Congratulations to both player for this draw...")
