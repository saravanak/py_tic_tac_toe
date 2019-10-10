from tic_tac_toe import TicTacToe

import unittest

class TicTacToeTest(unittest.TestCase):

    def test_initial_state(self):
        t = TicTacToe()
        t.game = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        (is_game_complete, winner)  = t.is_game_complete()
        self.assertFalse(is_game_complete)
        self.assertEqual(winner, None)

    def test_horizontal_wins(self):
        t = TicTacToe()
        t.game = [
            ['X', 'X', 'X'],
            ['', '', ''],
            ['', '', '']
        ]
        (is_game_complete, winner)  = t.is_game_complete()
        self.assertTrue(is_game_complete)
        self.assertEqual(winner, 'X')

    def test_vertical_wins(self):
        t = TicTacToe()
        t.game = [
            ['X', '', 'X'],
            ['', '', 'X'],
            ['', '', 'X']
        ]
        (is_game_complete, winner)  = t.is_game_complete()
        self.assertTrue(is_game_complete)
        self.assertEqual(winner, 'X')

    def test_diagonal_wins(self):
        t = TicTacToe()
        t.game = [
            ['X', '', 'X'],
            ['', 'X', '0'],
            ['', '', 'X']
        ]
        (is_game_complete, winner)  = t.is_game_complete()
        self.assertTrue(is_game_complete)
        self.assertEqual(winner, 'X')
