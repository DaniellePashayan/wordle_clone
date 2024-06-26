import pygame

from settings import *
from game import Game

class Letter:
    def __init__(self, text: str, bg_position: tuple, bg_color:str = "white", text_color:str="black") -> None:
        # sets the default values
        self.bg_color = bg_color
        self.text_color = text_color
        
        # passes in the position of where the letter will be placed
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (self.bg_x, self.bg_y, KEYBOARD_LETTER_SIZE, KEYBOARD_LETTER_SIZE)
        
        # sets the text and the position of the text
        self.text = text
        self.text_position = (self.bg_x, self.bg_y)
        
        # loads the fonts
        self.GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
        self.AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)
        
        # renders the text
        self.text_surfcae = self.GUESSED_LETTER_FONT.render(text, True, pygame.Color(self.text_color))
        self.text_rect = self.text_surfcae.get_rect(center=self.text_position)
    
    def draw(self):
        # puts the letter and the corresponding letter on the screen in the desired location on the screen
        pygame.draw.rect(Game.SCREEN, pygame.Color(self.bg_color), self.bg_rect)
        if self.bg_color == 'white':
            pygame.draw.rect(Game.SCREEN, DARK_GRAY, self.bg_rect, 2)
        self.text_surface = self.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        Game.SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()
    
    def delete(self):
        # replaces the letter with a white rectangle
        pygame.draw.rect(Game.SCREEN, pygame.Color("white"), self.bg_rect)
        pygame.draw.rect(Game.SCREEN, DARK_GRAY, self.bg_rect, 2)
        pygame.display.update()