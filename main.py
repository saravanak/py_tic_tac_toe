from curses import wrapper, newwin
import curses
from tic_tac_toe import SIZE, TicTacToe
from tic_tac_toe_renderer import TicTacToeRenderer

def main(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.addstr("Hello Curses")

    begin_x = 20; begin_y = 7
    height = 5; width = 10

    stdscr.refresh()

    ttt = TicTacToe()
    renderer = TicTacToeRenderer(ttt, stdscr, height, width, begin_y, begin_x)

    while not renderer.is_game_complete:
        renderer.render()
        stdscr.refresh()
        move = stdscr.getch()
        renderer.move(move)

    renderer.render()
    stdscr.refresh()
    stdscr.addstr("Winner Is: %s" % (renderer.winner))
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
