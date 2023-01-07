"""
    This file contains a class that represents information of current score
    and best score of the game.
"""
import pygame.font
class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 125, 50
        self.board_color = (215, 145, 66)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)
        self.rect = pygame.Rect(self.screen_rect.right - 130, 5, self.width, self.height)
        self.high_rect = pygame.Rect(188, 5, self.width, self.height)
        self.prep_score()
        self.prep_high_score()
        
    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = "Score: "+"{:,}".format(self.game.curr_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.board_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.center = self.rect.center
    
    def show_score(self):
        """Prepare and draw scores to the screen."""
        self.prep_score()
        self.prep_high_score()
        self.screen.fill(self.board_color, self.rect)
        self.screen.fill(self.board_color, self.high_rect)
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_str = "Best: " + "{:,}".format(self.game.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.board_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_image_rect.top
    
    
