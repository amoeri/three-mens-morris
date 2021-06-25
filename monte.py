import copy

from random import choice
from game import Board


class MonteCarlo:
    def __init__(self, id, max_simulations):
        """ Takes an instance of a board and optionally some keyword arguments.
        Initializes the list of games states and the statistics table. """
        self.id = id
        self.name = "Player " + str(id) + " (Monte, sim: " + str(max_simulations) + ")"

        self.max_simulations = max_simulations
        self.plays = {}
        self.wins = {}

    def getNextMove(self, player, board):
        """ Causes the AI to calculate the best move from the current game state
        and return it. """
        board_copy = Board(copy.deepcopy(board.board))
        return self._run_simulation(player, board_copy)

    def getMove(self, player, board):
        next_moves = board.legalMoves(player)

        return next_moves

    def _run_simulation(self, player, board):
        evaluations = {}

        for t in range(self.max_simulations):
            current_player = player
            board_copy = Board(copy.deepcopy(board.board))

            simulation_moves = []

            next_moves = self.getMove(current_player, board_copy)

            score = 0

            while next_moves:
                random_move = choice(next_moves)
                board_copy.move(random_move)

                simulation_moves.append(random_move)

                if board_copy.winner() != 0:
                    break

                score -= 1

                current_player = current_player * -1
                next_moves = self.getMove(current_player, board_copy)

            first_move = simulation_moves[0]

            first_move_key = first_move

            if current_player == -1 and board_copy.winner() == -1:
                score -= 1

            if first_move_key in evaluations:
                evaluations[first_move_key] += score
            else:
                evaluations[first_move_key] = score

        best_move = []
        highest_score = 0
        first_round = True

        for move, score in evaluations.items():
            if first_round or score > highest_score:
                highest_score = score
                best_move = move
                first_round = False

        return best_move

