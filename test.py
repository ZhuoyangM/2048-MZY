"""
    This file contains unit tests of the logic of the game.
"""

from logic import *
import unittest
board = [[2, 4, 4, 2],
         [4, 0, 4, 4],
         [0, 2, 0, 2],
         [2, 0, 0, 2]]

dict = moveDown(board)
print(board)
print(dict)
