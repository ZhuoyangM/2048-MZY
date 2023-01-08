"""
    This file contains unit tests of game logic.
"""
from logic import *
import unittest
class TestGameLogic(unittest.TestCase):
    
    def test_moveLeft(self):
        '''Test move left functionality'''
        before = [[2, 4, 4, 2],
                   [4, 0, 4, 4],
                   [0, 2, 0, 2],
                   [2, 0, 0, 2]]
        after = [[2, 8, 2, 0],
                [8, 4, 0, 0],
                [4, 0, 0, 0],
                [4, 0, 0, 0]]
        dict = moveLeft(before)
        expected = {8:2, 4:2}
        self.assertEqual(before, after)
        self.assertEqual(dict, expected)
    
    def test_moveRight(self):
        '''Test move right functionality'''
        before = [[2, 4, 4, 2],
                   [4, 4, 2, 2],
                   [0, 2, 0, 2],
                   [2, 0, 0, 2]]
        after = [[0, 2, 8, 2],
                [0, 0, 8, 4],
                [0, 0, 0, 4],
                [0, 0, 0, 4]]
        dict = moveRight(before)
        expected = {8:2, 4:3}
        self.assertEqual(before, after)
        self.assertEqual(dict, expected)

    def test_moveUp(self):
        '''Test move up functionality'''
        before = [[2, 4, 4, 2],
                   [0, 4, 2, 2],
                   [0, 2, 0, 2],
                   [2, 0, 2, 2]]
        after = [[4, 8, 4, 4],
                [0, 2, 4, 4],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        dict = moveUp(before)
        expected = {4:4, 8:1}
        self.assertEqual(before, after)
        self.assertEqual(dict, expected)
    
    def test_moveDown(self):
        '''Test move down functionality'''
        before = [[2, 4, 4, 2],
                   [2, 4, 2, 0],
                   [0, 2, 0, 0],
                   [2, 2, 0, 2]]
        after = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [2, 8, 4, 0],
                [4, 4, 2, 4]]
        dict = moveDown(before)
        expected = {4:3, 8:1}
        self.assertEqual(before, after)
        self.assertEqual(dict, expected)

    def test_checkMerge(self):
        '''Test check for mergable tiles functionality'''
        board = [[2, 4, 4, 2],
                   [0, 4, 2, 2],
                   [0, 2, 0, 2],
                   [2, 0, 2, 2]]
        self.assertTrue(checkMerge(board))

    def test_checkMax(self):
        '''Test check for max tile functionality'''
        board = [[2, 4, 4, 2],
                   [0, 4, 2, 2],
                   [0, 2, 0, 2],
                   [2, 0, 2, 2]]
        self.assertFalse(checkMax(board))
    
    def test_checkEmpty(self):
        '''Test check for empty tiles functionality'''
        board = [[2, 4, 4, 2],
                   [0, 4, 2, 2],
                   [0, 2, 0, 2],
                   [2, 0, 2, 2]]
        self.assertTrue(checkEmpty(board))

    def test_reverse(self):
        '''Test the reverse functionality'''
        before = [[2, 4, 4, 2],
                   [0, 4, 2, 2],
                   [0, 2, 0, 2],
                   [2, 0, 2, 2]]
        after =[[2, 4, 4, 2],
                [2, 2, 4, 0],
                [2, 0, 2, 0],
                [2, 2, 0, 2]]
        reverse(before)
        self.assertEqual(before, after)


    def test_transpose(self):
        '''Test the transpose functionality'''
        before = [[2, 4, 4, 2],
                   [0, 4, 2, 2],
                   [0, 2, 0, 2],
                   [2, 0, 2, 2]]
        after =[[2, 0, 0, 2],
                [4, 4, 2, 0],
                [4, 2, 0, 2],
                [2, 2, 2, 2]]
        transpose(before)
        self.assertEqual(before, after)
    
    def test_compress(self):
        '''Test the compress functionality'''
        before = [[2, 0, 0, 4],
                   [0, 4, 2, 2],
                   [0, 2, 0, 2],
                   [2, 0, 2, 2]]
        after =[[2, 4, 0, 0],
                [4, 2, 2, 0],
                [2, 2, 0, 0],
                [2, 2, 2, 0]]
        compress(before)
        self.assertEqual(before, after)

    def test_merge(self):
        '''Test the merge functionality'''
        before =[[2, 4, 0, 0],
                [4, 2, 2, 0],
                [2, 2, 0, 0],
                [2, 2, 2, 0]]
        after = [[2, 4, 0, 0],
                 [4, 4, 0, 0],
                 [4, 0, 0, 0],
                 [4, 2, 0, 0]]
        merge(before)
        self.assertEqual(before, after)

if __name__ == '__main__':
    unittest.main()


