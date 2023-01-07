"""
    This file contains a class that represents a button on the game board.
"""
import pygame.font
class Button:
    '''Class used to represent a button.'''
    def __init__(self, game, msg):
        """Initialize button attributes."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 125, 50
        self.button_color = (215, 145, 66)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)
        self.rect = pygame.Rect(5, 5, self.width, self.height)
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw a blank button and then display message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)