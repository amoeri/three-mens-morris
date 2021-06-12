import sys, os
import itertools

from datetime import datetime

from play import play

USAGE = """
Usage: tournament.py [NUMBEROFGAMES]

This will start a tournament in which every existing bot (agent) plays against each other once. The results of all games
played will be stored in a file called `tournament.results`.

NUMBEROFGAMES
  Number of rounds each bot has to play against another bot. Defaults to 1'000.
"""

# PARTICIPATING_AGENT_IDENTIFIERS = ['random', 'minimax', 'reader+minimax', 'reader+random']
PARTICIPATING_AGENT_IDENTIFIERS = ['random', 'minimax', 'reader+minimax']

if len(sys.argv) not in range(1,3):
  print(USAGE)
  sys.exit()

NUMBER_OF_GAMES = 1 if len(sys.argv) != 2 else int(sys.argv[1])

print(f"Starting a new tournament with {NUMBER_OF_GAMES} round(s) for each bot encounter.")
print(f"Participating agents: {PARTICIPATING_AGENT_IDENTIFIERS}")

f = open("tournament.results", "a")
start = datetime.now()
f.write("============================= " + start.strftime("%d.%m.%Y %H:%M:%S") + " =========================================\n")
f.write(f"Starting a new tournament with {NUMBER_OF_GAMES} games for each match...\n")
f.flush()

# Iterate over all possible combinations of participating agents and let them play against each other.
for agent0, agent1 in itertools.combinations(PARTICIPATING_AGENT_IDENTIFIERS, 2):
  print(f"{agent0} vs {agent1}")
  result = play(['play.py', agent0, agent1, str(NUMBER_OF_GAMES)])
  f.write(f"({result['duration']}) {result['agent0']} VS {result['agent1']} => {result['agent0_wins']}:{result['agent1_wins']}\n")
  f.flush()

f.write("Tournament finished in " + str(datetime.now() - start) + "\n" )
f.close()

print("Tournament is over. Results are stored in `tournament.results`.")
