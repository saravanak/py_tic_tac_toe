from tic_tac_toe import SIZE
import curses

class TicTacToeRenderer(object):
    def __init__(self, tic_tac_toe, stdscr, height, width, begin_y, begin_x):
        self.tic_tac_toe = tic_tac_toe

        self.tile_center = (height / 2 - 1, width/2 - 1)

        self.tiles = [[stdscr.subwin(height, width, begin_y + (i * height), begin_x + (j * width)) for j in range(0, SIZE)] for i in range(0, SIZE)]

    def render(self):
        for i in range(0, SIZE):
            for j in range(0, SIZE):
                tile = self.tiles[i][j]
                player_token = self.tic_tac_toe.game[i][j]
                tile.clear()
                tile.addch(self.tile_center[0], self.tile_center[1], 32 if player_token == '' else player_token)
                tile.box(0,0)
                if self.current_position == (i, j):
                    tile.addch('>', curses.A_BLINK)

                tile.noutrefresh()

    @property
    def current_position(self):
        return self.tic_tac_toe.current_position

    @property
    def is_game_complete(self):
        return self.tic_tac_toe.is_game_complete()[0]

    @property
    def winner(self):
        return self.tic_tac_toe.is_game_complete()[1]

    @current_position.setter
    def current_position(self, current_position):
        self.tic_tac_toe.current_position = current_position

    def move(self, move_direction):
        if move_direction == 10: #New line
            self.tic_tac_toe.take_current_tile()
            return

        current_offset = self.current_position[0] * SIZE + self.current_position[1]
        if move_direction == curses.KEY_LEFT:
            current_offset -= 1
        elif move_direction == curses.KEY_RIGHT:
            current_offset += 1
        elif move_direction == curses.KEY_UP:
            current_offset -= SIZE
        elif move_direction == curses.KEY_DOWN:
            current_offset += SIZE
        else:
            return

        if current_offset < 0:
            current_offset = 0

        if current_offset >= pow(SIZE, 2) - 1:
            current_offset = pow(SIZE, 2) - 1

        self.current_position = (current_offset / SIZE, current_offset % SIZE)
