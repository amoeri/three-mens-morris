import logging
logging.basicConfig(filename='games.log', encoding='utf-8', level=logging.DEBUG)

from datetime import datetime

now = datetime.now()

from random import Random
from game import Game

from human import Human
from minimax import Minimax
from rando import Rando
from reader import Reader

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
      p.append(Minimax(i - 1, 7))
    case "reader+minimax":
      p.append(Reader(i - 1, Minimax(i - 1, 7)))
    case "reader+random":
      p.append(Reader(i - 1, Rando(i - 1)))

games = 1
if n == 4:
  games = int(sys.argv[3])

logging.info("New run starting at " + str(now))


print("Starting " + str(games) + " game(s) between " + p[0].name + " and " + p[1].name)
logging.info("Starting " + str(games) + " game(s) between " + p[0].name + " and " + p[1].name)

wins = [0, 0]
for gamenr in range(games):
  print("Starting game #" + str(gamenr))
  logging.info("Starting game #" + str(gamenr))
  if (gamenr % 2) == 0:
    game = Game(p[0], p[1])
  else:
    game = Game(p[1], p[0])
  winner = game.start()
  wins[winner.id] += 1
  print("And the winner of game #" + str(gamenr) +" is " + str(winner.name))
  logging.info("And the winner of game #" + str(gamenr) +" is " + str(winner.name))

if games > 1:
  print("The series of " + str(games) + " games is over.")
  logging.info("The series of " + str(games) + " games is over.")
  print(p[0].name + " has won " + str(wins[0]) + " time(s) and " + p[1].name + " has won " + str(wins[1]) + " time(s)")
  logging.info(p[0].name + " has won " + str(wins[0]) + " time(s) and " + p[1].name + ") has won " + str(wins[1]) + " time(s)")
  if wins[0] > wins[1]:
    print("Congratulations to " + p[0].name + "!!!")
  elif wins[1] > wins[0]:
    print("Congratulations to " + p[1].name + "!!!")
  else:
    print("Congratulations to both players for this draw...")
