import pygame

from src.settings import *

class Indicator:
    def __init__(self, x, y, letter, screen):
        self.x = x
        self.y = y
        self.letter = letter
        self.rect = (self.x, self.y, INDICATOR_SIZE, INDICATOR_SIZE)
        self.bg_color = LIGHT_GRAY
        self.screen = screen

        
    def draw(self):
        # puts the placeholder and text on the screen at the desired location
        pygame.draw.rect(self.screen, pygame.Color(self.bg_color), self.rect)
        self.text_surface = pygame.font.Font(FONT, 50).render(self.letter, True, pygame.Color("white"))
        self.text_rect = self.text_surface.get_rect(center=(self.x+25, self.y+25))
        self.screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()
        