import math
import random

PLAYER_SYMBOLS = [ 'X', 'O' ]

"""
Abstract Player class
"""
class APlayer():
    def __init__(self, symbol):
        assert symbol in PLAYER_SYMBOLS
        self.symbol = symbol

    def get_move(self, _game):
        # abstract method
        pass

    def __str__(self):
        return f'{self.symbol}'

"""
Human Player Concrete class
"""
class HPlayer(APlayer):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        val = None
        while True:
            cell = input(self.symbol + f'\'s turn. Input move (0-{game.n}): ')
            try:
                val = int(cell)
                if val not in game.available_moves():
                    raise ValueError
                break
            except ValueError:
                print('Invalid cell number. Try again.')
        return val

"""
Random Player Concrete class
"""
class RPlayer(APlayer):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        return random.choice(game.available_moves())

"""
Computer Player Concrete class, using minimax to
make decision about best move to do
"""
class CPlayer(APlayer):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        if len(game.available_moves()) == game.n:    ## first move...
            cell = random.choice(game.available_moves())
        else:
            hsh = self._minimax_a_b(game, self.symbol)
            cell = hsh['position']
            assert cell is not None, f"got {hsh} !"
        return cell

    def _minimax(self, state, cplayer):
        """
        given the state (of game) and the c(urrent) player (as represented by its symbol)
        select best possible moves using minimax exploration

        Note: for tic tac toe the upper bound for the size of the state space is 3**9 = 19_683
        """
        ## determine roles
        max_player = self.symbol                          ## maximize our score...
        oth_player = 'X' if cplayer == 'O' else 'O'       ## ...while minimizing the other player score

        ## base case for recursion of minmax
        if state.current_winner == oth_player:
            ## need to return a pos. and score to complete base case of recursion
            return {'position': None,
                    'score': self._score_fn(state, max_player, oth_player)}

        elif not state.empty_cells():                     ## no empty cells left... No winner
            return {'position': None, 'score': 0}

        ## now recurrence
        ## 1 - init dictionary (once per level of depth first search)
        if cplayer == max_player:
            best = {'position': None, 'score': -math.inf} ## want to maximize this
        else:
            ## oth_player
            best = {'position': None, 'score': math.inf}  ## want to minimize this
        ##
        ## 2 - launch recursive exploration to eval the best score
        for poss_move in state.available_moves():
            state.make_move(poss_move, cplayer)           ## play the (possible) move for (current) player => mutate state
            sim_score = self._minimax(state, oth_player)  ## given current state, simulate best move for oth(er) player => a dfs
            sim_score['position'] = poss_move             ## mark (current possible) position

            ## conclude
            if cplayer == max_player:
                if sim_score['score'] > best['score']: best = sim_score
            else:
                # oth_player
                if sim_score['score'] < best['score']: best = sim_score
            ##
            ## reset explored moves
            state.board[poss_move] = state.__class__.EMPTY_SYMB
            state.current_winner = None
        #
        return best

    def _minimax_a_b(self, state, cplayer, alpha=-math.inf, beta=math.inf):
        """
        minimax + α-β pruning
        """
        ## determine roles
        max_player = self.symbol
        oth_player = 'X' if cplayer == 'O' else 'O'

        ## base case for recursion of minmax
        if state.current_winner == oth_player:
            return {'position': None,
                    'score': self._score_fn(state, max_player, oth_player)}
        elif not state.empty_cells():
            return {'position': None, 'score': 0}

        ## now recurrence
        best = {'position': None, 'score': -math.inf} if cplayer == max_player \
            else {'position': None, 'score': math.inf}

        for poss_move in state.available_moves():
            state.make_move(poss_move, cplayer)
            sim_score = self._minimax_a_b(state, oth_player, alpha, beta)
            sim_score['position'] = poss_move

            if cplayer == max_player:
                if sim_score['score'] > best['score']: best = sim_score

                alpha = max(alpha, best['score'])
                if alpha >= beta:
                    self._reset_state(state, poss_move)
                    break  ## β-cutoff
            else:
                # oth_player
                if sim_score['score'] < best['score']: best = sim_score

                beta = min(beta, best['score'])
                if beta <= alpha:
                    self._reset_state(state, poss_move)
                    break  ## α-cutoff
            ##
            ## reset explored moves
            self._reset_state(state, poss_move)
        #
        return best

    def _reset_state(self, state, move):
        state.board[move] = state.__class__.EMPTY_SYMB
        state.current_winner = None
        return

    @staticmethod
    def _score_fn(game, max_player, oth_player):
        f = 1 if max_player == oth_player else -1
        return f * (game.num_empty_cells() + 1)
