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
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    BACKGROUND = pygame.image.load("assets/blank.png")
    aspect_ratio = BACKGROUND.get_width() / BACKGROUND.get_height()

    new_width = 500
    new_height = new_width / aspect_ratio
    BACKGROUND = pygame.transform.scale(BACKGROUND, (new_width, new_height))  # Replace new_width and new_height with your desired dimensions
    BACKGROUND_RECT = BACKGROUND.get_rect(center=(WIDTH // 2, 350))

    game_loop()

if __name__ == "__main__":
    main()