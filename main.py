import pygame
import sys
from src.game import Game
from src.settings import *

def main():
    pygame.init()
    
    # sets up the window display
    pygame.display.set_caption("PyWordle - DaniellePashayan")
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    ICON = pygame.image.load("assets/Icon.png")
    pygame.display.set_icon(ICON)

    # loads the background placeholder image, resizes, and centers it
    BACKGROUND = pygame.image.load("assets/blank.png")
    aspect_ratio = BACKGROUND.get_width() / BACKGROUND.get_height()
    new_width = 400
    new_height = new_width / aspect_ratio
    BACKGROUND = pygame.transform.scale(BACKGROUND, (new_width, new_height))
    BACKGROUND_RECT = BACKGROUND.get_rect(center=(WIDTH // 2, 300))
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    return SCREEN

if __name__ == "__main__":
    screen = main()
    
    game = Game(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key_pressed = event.unicode.upper()
                if key_pressed in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if len(game.current_guess_string) < 5:
                        print(key_pressed)
                        game.draw_letter(key_pressed)

        pygame.display.update()
    
