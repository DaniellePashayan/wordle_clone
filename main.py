import pygame
import sys
import random

from src.utility import get_word_list_from_file
from src.settings import *


def main():
    def game_loop():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            SCREEN.fill("white")
            SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
            pygame.display.update()
        
    pygame.init()
    
    # sets up the window display
    pygame.display.set_caption("PyWordle - DaniellePashayan")
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    
    # loads the fonts
    GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
    AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)
    
    # loads the background placeholder image, resizes, and centers it
    BACKGROUND = pygame.image.load("assets/blank.png")
    aspect_ratio = BACKGROUND.get_width() / BACKGROUND.get_height()
    new_width = 400
    new_height = new_width / aspect_ratio
    BACKGROUND = pygame.transform.scale(BACKGROUND, (new_width, new_height))
    BACKGROUND_RECT = BACKGROUND.get_rect(center=(WIDTH // 2, 300))

    game_loop()

if __name__ == "__main__":
    main()