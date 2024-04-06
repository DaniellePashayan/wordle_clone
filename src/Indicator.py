import pygame

from src.settings import *

class Indicator:
    def __init__(self, x: int, y: int, letter: str, screen: pygame.Surface, width:int, height:int, font_size:int,bg_color:str=LIGHT_GRAY, text_color:str = pygame.Color("black"), outline_color:str=pygame.Color("black")):
        self.x = x
        self.y = y
        self.letter = letter
        self.height = height
        self.width = width
        self.rect = (self.x, self.y, width, height)
        self.screen = screen
        self.bg_color = bg_color
        self.text_color = text_color
        self.outline_color = outline_color
        self.font_size = font_size

        
    def draw(self):
        # puts the placeholder and text on the screen at the desired location
        
        pygame.draw.rect(self.screen, self.bg_color, self.rect, border_radius=2)
        self.text_surface = pygame.font.Font(FONT, self.font_size).render(self.letter, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(self.text_surface, self.text_rect)
        