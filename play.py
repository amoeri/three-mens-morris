import logging
logging.basicConfig(filename='games.log', encoding='utf-8', level=logging.DEBUG)

from datetime import datetime

USAGE = """
Usage: play.py PLAYER0 PLAYER1 [NUMBEROFGAMES]

PLAYER0/PLAYER1
  Must be identifierts for agents that `play.py` knows of, such as:
  - human
  - random
  - minimax
  - reader+minimax
  - reader+random
"""

from random import Random
from game import Game

from human import Human
from minimax import Minimax
from monte import MonteCarlo
from rando import Rando
from reader import Reader

import sys

should_log_to_stdout = False


def play(args):
  now = datetime.now()

  def log_to_stdout(string):
    if should_log_to_stdout:
      print(string)

  p = []
  n = len(args)
  result_data = {
    'agent0': None,
    'agent1': None,
    'games': None,
    'agent0_wins': None,
    'agent1_wins': None,
    'duration': None
  }

  if n < 3 or n > 4:
    print(USAGE)
    sys.exit()

  for i in range(1, 3):
    match args[i]:
      case "human":
        p.append(Human(i - 1))
      case "random":
        p.append(Rando(i - 1))
      case "minimax":
        p.append(Minimax(i - 1, 7))
      case "monte":
        p.append(MonteCarlo(i - 1, 1000))
      case "reader+minimax":
        p.append(Reader(i - 1, Minimax(i - 1, 7)))
      case "reader+random":
        p.append(Reader(i - 1, Rando(i - 1)))
      case _:
        print("Agent identifier ('" + args[i] + "') unknown")
        sys.exit()

  games = 1
  if n == 4:
    games = int(args[3])

  logging.info("New run starting at " + str(now))

  log_to_stdout("Starting " + str(games) + " game(s) between " + p[0].name + " and " + p[1].name)
  logging.info("Starting " + str(games) + " game(s) between " + p[0].name + " and " + p[1].name)

  result_data['agent0'] = p[0].name
  result_data['agent1'] = p[1].name
  result_data['games'] = games


  wins = [0, 0]
  for gamenr in range(games):
    log_to_stdout("Starting game #" + str(gamenr))
    logging.info("Starting game #" + str(gamenr))
    if (gamenr % 2) == 0:
      game = Game(p[0], p[1])
    else:
      game = Game(p[1], p[0])
    winner = game.start()
    wins[winner.id] += 1
    log_to_stdout("And the winner of game #" + str(gamenr) +" is " + str(winner.name))
    logging.info("And the winner of game #" + str(gamenr) +" is " + str(winner.name))

  if games > 1:
    log_to_stdout("The series of " + str(games) + " games is over.")
    logging.info("The series of " + str(games) + " games is over.")
    log_to_stdout(p[0].name + " has won " + str(wins[0]) + " time(s) and " + p[1].name + " has won " + str(wins[1]) + " time(s)")
    logging.info(p[0].name + " has won " + str(wins[0]) + " time(s) and " + p[1].name + ") has won " + str(wins[1]) + " time(s)")
    if wins[0] > wins[1]:
      log_to_stdout("Congratulations to " + p[0].name + "!!!")
    elif wins[1] > wins[0]:
      log_to_stdout("Congratulations to " + p[1].name + "!!!")
    else:
      log_to_stdout("Congratulations to both players for this draw...")
      
  result_data['agent0_wins'] = wins[0]
  result_data['agent1_wins'] = wins[1]
  result_data['duration'] = datetime.now() - now

  result_data

  return result_data


# Only start a new game when this script is explicitly called, so we can import the `play` function from other files
# without immediately triggering the execution of the code.
# TODO: Remove first argument (prog name...).
if __name__ == '__main__':
  should_log_to_stdout = True
  play(sys.argv)

