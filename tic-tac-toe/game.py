import math
import time
from  player import HPlayer, RPlayer, CPlayer

"""
Game represent the tic-tac-toe game
"""
class Game():
    EMPTY_SYMB = '_'
    GAME_DEF_DIM = 3

    def __init__(self, n=GAME_DEF_DIM):
        self.n = n
        self.board = self._create_board(n, __class__.EMPTY_SYMB)
        self.current_winner = None

    def make_move(self, cell, symbol):
        assert cell is not None
        if self.board[cell] == __class__.EMPTY_SYMB:
            self.board[cell] = symbol
            # is it a win?
            if self.winner(cell, symbol):
                self.current_winner = symbol
            return True
        return False  # cell already played

    def winner(self, cell, symbol):
        """
        any self.n aligned symbol, wether horizonatally, vertically or diagonally
        """
        # 1 - check rows
        return self.win_row(cell, symbol) or self.win_col(cell, symbol) \
            or self.win_diag(cell, symbol)

    def empty_cells(self):
        return __class__.EMPTY_SYMB in self.board

    def num_empty_cells(self):
        return self.board.count(__class__.EMPTY_SYMB)

    def available_moves(self):
        return [ix for ix, c in enumerate(self.board) if c == __class__.EMPTY_SYMB]

    def display_board(self):
        n = self.n
        n_dig = math.ceil(math.log(n) / math.log(10)) + 1
        npre, npost = math.floor((n_dig + 1) / 2), math.ceil((n_dig + 1) / 2)
        print(('|' + '-' * (n_dig + 2)) * n + '|')
        srow = ''
        for row in range(0, n):
            for c in range(row * n, (row + 1) * n):
                srow += '|' + ' ' * npre + self.board[c] + ' ' * npost
            srow += '|\n'
            srow += ('|' + '-' * (n_dig + 2)) * n + '|\n'
        print(srow)
        print()
        return

    def display_board_num(self):
        """
        display with num. to help select a cell to play...

        |---|---|---|
        | 0 | 1 | 2 |
        |---|---|---|
        | 4 | 5 | 6 |
        |---|---|---|
        | 7 | 8 | 9 |
        |---|---|---|

        |-----|-----|-----|-----|-----|
        |  0  |  1  |  2  |  3  |  4  |
        |-----|-----|-----|-----|-----|
        |  5  |  6  |  7  |  8  |  9  |
        |-----|-----|-----|-----|-----|
        | 10  | 11  | 12  | 13  | 14  |
        |-----|-----|-----|-----|-----|
        | 15  | 16  | 17  | 18  | 19  |
        |-----|-----|-----|-----|-----|
        | 20  | 21  | 22  | 23  | 24  |
        |-----|-----|-----|-----|-----|

        """
        n = self.n
        n_dig = math.ceil(math.log(n) / math.log(10)) + 1

        # num_board = [
        #    [str(ix) for ix in range(jx * n, (jx+1) * n)] for jx in range(n)
        #]
        num_board = []
        for jx in range(n):
            row = []
            for ix in range(jx * n, (jx+1) * n):
                s = str(ix)
                q, r = divmod(n_dig - len(s), 2)
                row.append(' ' * q + s + ' ' * r)
            num_board.append(row)

        print(('|' + '-' * (n_dig + 2)) * n + '|')
        for row in num_board:
            print('| ' + ' | '.join(row) + ' |')
            print(('|' + '-' * (n_dig + 2)) * n + '|')
        print()
        return

    ## Private Helpers
    @staticmethod
    def _create_board(n, symb):
        return [symb for _ in range(n * n)]

    def win_row(self, cell, symbol):
        rn = cell // self.n   # math.floor(cell / self.n)
        # for rn in range(0, self.n):
        r = self.board[rn * self.n:(rn + 1) * self.n]
        if ''.join(r) == symbol * self.n:
            return True
        return False

    def win_col(self, cell, symbol):
        cn = cell % self.n   # column number (index)
        ulim = self.n * self.n + cn
        sc = ''.join([self.board[c] for c in range(0 + cn, ulim, self.n)])
        if sc == symbol * self.n:
            return True
        return False

    def win_diag(self, cell, symbol):
        # up
        upd = [d * (self.n - 1) for d in range(1, self.n + 1)]
        if cell in upd and ''.join([self.board[x] for x in upd]) ==  symbol * self.n:
            return True
        # down
        down = [d * (self.n + 1) for d in range(0, self.n)]
        if cell in down and ''.join([self.board[x] for x in down]) ==  symbol * self.n:
            return True
        return False

## Client
def play(game, x_player, o_player, disp_game=True):
    if disp_game: game.display_board_num()
    symbol = 'X'
    while game.empty_cells():
        cell = o_player.get_move(game) if symbol == 'O' else x_player.get_move(game)

        if game.make_move(cell, symbol):
            if disp_game:
                print(symbol + ' plays move to cell {}'.format(cell))
                game.display_board()
                print('')

            if game.current_winner:
                if disp_game:
                    print(symbol + ' wins!')
                return symbol  # end of the game

            # next turn
            symbol = 'O' if symbol == 'X' else 'X'
        #
        if disp_game: time.sleep(0.6)
    #
    if disp_game: print('Tie!')
    return None

def simulation(ng, n=3):
    o_nwin, x_nwin, n_tie = 0, 0, 0
    x_player = RPlayer('X')
    o_player = CPlayer('O')

    for ix in range(1, ng+1):
        # if ix % 100 == 0:
        #     print(f"played {ix} / {ng}")
        game = Game(n)
        outcome = play(game, x_player, o_player, disp_game=False)

        if outcome is None:
            n_tie += 1
        elif outcome == 'O':
            o_nwin += 1
        else:
            x_nwin += 1
    print(f"o_wins: {o_nwin}, x_wins: {x_nwin}, n_ties: {n_tie}")
    return (o_nwin, x_nwin, n_tie)

def interactive_play(n=Game.GAME_DEF_DIM):
    x_player = RPlayer('X')
    o_player = CPlayer('O')
    game = Game(n)
    play(game, x_player, o_player)

if __name__ == '__main__':
    # interactive_play(3)   ## for n > 3 => slow search!
    simulation(1000)

#
# o_wins: 808, x_wins: 0, n_ties: 192
# 
# real    3m25.108s
# user    3m25.098s
# sys     0m0.009s
#
