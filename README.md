# Three men's morris
BFH BTI7501p semester project

## Game rules
[Wikipedia](https://en.wikipedia.org/wiki/Three_men%27s_morris)
This project uses the rules where a stone can only be move to adjacent spots.

## Requirements
- Python 3.10, currently (2021-05-21) only available as developer preview [here](https://www.python.org/downloads/release/python-3100a7/)

## Project setup
The project is very simple.
`game.py` implements the game according to the rules mentioned above within two classes:
1. `Game` which takes two players and let's them play against each other. The firt player passed will be going first.
2. `Board` which represents the current board state and has a nice `__str__` method.

`play.py` is the main script and helps set up games between players.
It can be run with `py play.py PLAYER0 PLAYER1 [NUMBEROFGAMES]`
`PLAYER0`/`PLAYER1` must be identifiers for agents that `play.py` knows of, such as:
- `human`
- `minimax`
`NUMBEROFGAMES` defines how many games will be played. Players will alternate their starting turn. Default value is `1`.
`play.py` will also print whenever a game is started and ended to the terminal, aswell as a score total if more than one game is played.

### Agents
Any agent can be added playing different strategies.
It must implement:
1. A constructor that takes one parameter (id) which will be 0 or 1
2. Fields `id` (passed to the constructor) and `name` (A string identifying what type of agent it is, ideally also include the id in the name)
3. A method `getNextMove(self, player, board)` where:
  - `player` is the identifier used on the board during this game for that player (either -1 or 1)
  - `board` is an Object of type Board as defined in `game.py`
  - the method returns a valid move, which can either be:
    1. A tupel `(player, (x, y))` to set a stone (in the starting phase of the game), where `player` is the identifier passed to the method and `x` and `y` are the coordinates of the the position on the board (0, 1, 2), `x` beeing the row and `y` beeing the column
    2. A tupel `((x1, y1), (x2, y2))` to move a stone from x1, y1 to x2, y2 during the second phase of the game.
  - It is strongly encouranges to use the boards `legalMoves` method to get a list of the playable moves

There are currently no checks in place if the moves returned are acutally legal.

