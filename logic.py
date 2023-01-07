"""
    This file contains functions that implement the logic of 2048 game.
    These functions will be imported and used by the main file which runs
    the actual game.
"""

import random

def checkMax(board, max_tile = 2048):
    '''Check if the max tile is achieved.'''
    flat_board = [num for row in board for num in row]
    if max_tile in flat_board:
        return True
    else:
        return False

def checkEmpty(board):
    '''Check if an empty cell exists.'''
    flat_board = [num for row in board for num in row]
    if 0 in flat_board:
        return True
    else:
        return False

def checkMerge(board):
    '''Check if there are mergeable tiles.'''
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1] and board[i][j] != 0:
                return True
    for j in range(4):
        for i in range(3):
            if board[i][j] == board[i+1][j] and board[i][j] != 0:
                return True
    return False

def checkGameStatus(board, max_tile = 2048):
    '''Check the current game status'''
    won = checkMax(board, max_tile)
    if won:
        return 'WON'
    play = checkMerge(board) or checkEmpty(board)
    if play:
        return 'GAME IN PROGRESS'
    else:
        return 'LOST'

def fillNumber(board):
    '''Fill 2 or 4 in an empty cell of the board.'''
    flat_board = [num for row in board for num in row]
    i = random.randint(0,3)
    j = random.randint(0,3)
    while board[i][j] != 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
    if sum(flat_board) in (0,2):
        board[i][j] = 2
    else:
        board[i][j] = random.choice((2,4))
    return board

def diff(A, B):
    '''Check if boards A and B are different.'''
    for i in range(4):
        for j in range(4):
            if A[i][j] != B[i][j]:
                return True
    return False

def new_board():
    '''Generate a new game board.'''
    board = [[0] * 4 for _ in range(4)]
    fillNumber(board)
    fillNumber(board)
    return board

def compress(board):
    '''Compress the game board. '''
    for i in range(4):
        pos = 0
        for j in range(4):
            if board[i][j] != 0 and pos != j:
                board[i][pos] = board[i][j]
                board[i][j] = 0
                pos += 1
            elif board[i][j] != 0 and pos == j:
                pos += 1
    return board

def merge(board):
    '''Merge all mergeable tiles and return a dictionary of those tiles.'''
    merged_tiles = {}
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j+1] = 0
                if board[i][j] in merged_tiles:
                    merged_tiles[board[i][j]] += 1
                else:
                    merged_tiles[board[i][j]] = 1
    compress(board)
    return merged_tiles

def transpose(board):
    '''Transpose the game board.'''
    temp = []
    for i in range(4):
        temp.append([0] * 4)
    for i in range(4):
        for j in range(4):
            temp[j][i] = board[i][j]
    for i in range(4):
        for j in range(4):
            board[i][j] = temp[i][j]
    return board
        
def reverse(board):
    '''reverse each row of the game board.'''
    for i in range(4):
        l = 0
        h = 3
        row = board[i]
        while l < h:
            temp = row[l]
            row[l] = row[h]
            row[h] = temp
            l += 1
            h -= 1
    return board
        
def moveLeft(board):
    '''Move tiles to the left.'''
    compress(board)
    merged_tiles = merge(board)
    return merged_tiles


def moveRight(board):
    '''Move tiles to the right.'''
    reverse(board)
    compress(board)
    merged_tiles = merge(board)
    reverse(board)
    return merged_tiles

def moveUp(board):
    '''Move tiles up.'''
    transpose(board)
    compress(board)
    merged_tiles = merge(board)
    transpose(board)
    return merged_tiles


def moveDown(board):
    '''Move tiles down.'''
    transpose(board)
    reverse(board)
    compress(board)
    merged_tiles = merge(board)
    reverse(board)
    transpose(board)
    return merged_tiles

