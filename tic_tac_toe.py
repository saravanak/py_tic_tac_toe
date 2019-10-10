SIZE = 3
horizontals = lambda game: [game[i] for i in range(0, SIZE)]
verticals = lambda game: map(lambda i: [game[j][i] for j in range(0, SIZE)], range(0, SIZE))

def diagonals(game):
    return [
        [game[i][i] for i in range(0, SIZE)],
        [game[i][i] for i in range(SIZE - 1 ,-1, -1)]
    ]

PLAYERS = ['X', '0']
ALREADY_TAKEN = 999

class TicTacToe(object):
    def __init__(self):
        self.game = [['' for j in range(0, SIZE)] for i in range(0, SIZE)]
        self.current_player = '0' #|| 'X'
        self.current_position = (0, 0)

    def take_current_tile(self):
        current_tile = self.game[self.current_position[0]][self.current_position[1]]

        if current_tile == '':
            self.game[self.current_position[0]][self.current_position[1]] = self.current_player
        else:
            return ALREADY_TAKEN

        self.current_player = '0' if self.current_player == 'X' else 'X'

    def is_game_complete(self):
        checked_slices = []
        checked_slices += horizontals(self.game)
        checked_slices += verticals(self.game)
        checked_slices += diagonals(self.game)

        for current_player in PLAYERS:
            if any(map(lambda slice: all(map(lambda who: who == current_player, slice)), checked_slices)):
                return (True, current_player)

        return (False, None)
