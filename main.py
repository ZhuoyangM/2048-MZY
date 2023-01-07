"""
    This file contains a class that represents a 2048 game.
    To ran the game, simply run the script.
"""

import sys, pygame, json, time
from logic import *
from copy import deepcopy
from button import Button
from scoreboard import Scoreboard

class MyGame:
    '''Class used to represent a 2048 game. '''
    def __init__(self):
        '''Initialize a new game.'''
        pygame.init()
        
        self.c = json.load(open("settings.json", "r"))
        self.screen = pygame.display.set_mode((self.c["size"], self.c["size"] + 100))
        self.icon = pygame.transform.scale(pygame.image.load("images/icon.ico"), (32, 32))
        self.font = pygame.font.SysFont(self.c["font"], self.c["font_size"], bold=True)
        self.board = new_board()
        self.button = Button(self, msg = 'New Game')
        self.curr_score = 0
        self.high_score = 0 
        self.scoreboard = Scoreboard(self)
        self.status = 'GAME IN PROGRESS'
        
        pygame.display.set_caption("2048-MZY")
        pygame.display.set_icon(self.icon)

        
    def run_game(self):
        '''Run the main game loop.'''
        self.display_board()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    self.quit_game()
                elif event.type == pygame.KEYDOWN and self.status == 'GAME IN PROGRESS':
                    self.keydown_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN and self.status == 'GAME IN PROGRESS':
                    mouse_pos = pygame.mouse.get_pos()
                    button_clicked = self.button.rect.collidepoint(mouse_pos)
                    if button_clicked:
                        self.new_game()
            self.display_board()
            self.status = checkGameStatus(self.board, 2048)
            self.over_check(self.status)
    
    def over_check(self, status):
        '''Check if the game is over and display a corresponding message.'''
        if status != "GAME IN PROGRESS":
            size = self.c["size"]
            s = pygame.Surface((size, size), pygame.SRCALPHA)
            s.fill(self.c["color"]["over"])
            self.screen.blit(s, (0, 0))

            if status == "WON":
                msg = "YOU WIN!"
            else:
                msg = "YOU LOST!"

            self.screen.blit(self.font.render(msg, 1, (30, 30, 30)), (140, 180))
            self.screen.blit(self.font.render("Play again? (y/q)", 1, (30, 30, 30)), (80, 255))

            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                        self.quit_game()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                        self.new_game()
                        return
    

    def keydown_events(self, event):
        '''Check all key down events.'''
        old_board = deepcopy(self.board)
        dict = {}
        if event.key == pygame.K_LEFT:
            dict = moveLeft(self.board)
        elif event.key == pygame.K_RIGHT:
            dict = moveRight(self.board)
        elif event.key == pygame.K_UP:
            dict = moveUp(self.board)
        elif event.key == pygame.K_DOWN:
            dict = moveDown(self.board)
        for key in dict:
            self.curr_score += key * dict[key]
        if self.curr_score > self.high_score:
            self.high_score = self.curr_score
        if diff(old_board, self.board):
            fillNumber(self.board)
        
    def new_game(self):
        '''Start a new round of game.'''
        self.board = new_board()
        self.curr_score = 0
        self.status = 'GAME IN PROGRESS'
    
    def quit_game(self):
        '''Quit the game.'''
        pygame.quit()
        sys.exit()
    
    def display_board(self):
        '''Display the game board on the screen.'''
        self.screen.fill(tuple(self.c["color"]["background"]))
        box = self.c['size']//4
        padding = self.c["padding"]
        for i in range(4):
            for j in range(4):
                color = tuple(self.c["color"][str(self.board[i][j])])
                
                pygame.draw.rect(self.screen, color, pygame.Rect(j * box + padding,
                                                i * box + padding + 100,
                                                box - 2 * padding,
                                                box - 2 * padding), 0)
                if self.board[i][j] != 0:
                    if self.board[i][j] in (2, 4):
                        text_color = tuple(self.c["color"]["dark"])
                    else:
                        text_color = tuple(self.c["color"]["light"])
                    self.screen.blit(self.font.render("{:>4}".format(self.board[i][j]), 1, text_color),
                        (j * box + 2.5 * padding, i * box + 7 * padding + 100))
    
        self.button.draw_button()
        self.scoreboard.show_score()
        pygame.display.update()


if __name__ == '__main__':
    game = MyGame()
    game.run_game()
    
    
