import pygame
import sys
import random
from src.settings import *
from src.Indicator import Indicator

class Game:
    def __init__(self):
        pygame.init()

        # sets up the window display
        pygame.display.set_caption("PyWordle - DaniellePashayan")
        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.ICON = pygame.image.load("assets/Icon.png")
        pygame.display.set_icon(self.ICON)

        # loads the background placeholder image, resizes, and centers it
        self.BACKGROUND = pygame.image.load("assets/blank.png")
        aspect_ratio = self.BACKGROUND.get_width() / self.BACKGROUND.get_height()
        new_width = 400
        new_height = new_width / aspect_ratio
        self.BACKGROUND = pygame.transform.scale(self.BACKGROUND, (new_width, new_height))
        self.BACKGROUND_RECT = self.BACKGROUND.get_rect(center=(WIDTH // 2, 300))

        self.count_of_guesses = 0

        # each guess is going to be a list of 5 letters
        # each time the user makes a guess, it will be iterated over and each guess will be displayed to the screen
        self.guesses = [[]] * 6

        # stores the current guess, with each letter being a part of the array
        self.current_guess = []
        # stores the current guess as a string
        self.current_guess_string = ""

        self.current_letter_bg_x = 110

        # a list that stores the Indicator objects. the indicator is placeholder that will represent each letter
        self.indicators = []

        self.game_result = ""

    def draw_keyboard(self):
        indicator_x, indicator_y = 20, 500 #TODO
        # for i in range(len(KEYBOARD_ALPHABET)):
            # for letter in KEYBOARD_ALPHABET:
            #     new_ind = Indicator(indicator_x + 60, indicator_y + 60, letter, self.SCREEN)
            #     self.indicators.append(new_ind)
            #     new_ind.draw()
            #     indicator_x += 100
            # indicator_y +=100
            # if i == 0:
            #     indicator_x = 50
            # elif i == 1:
            #     indicator_x = 105
            # break
        for i in range(3):
            test = Indicator(indicator_x + 60, indicator_y + 60, "A", self.SCREEN)
            self.indicators.append(test)
            indicator_x += 100
        
        for indicator in self.indicators:
            indicator.draw()
            
            
    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.SCREEN.fill("white")
            self.SCREEN.blit(self.BACKGROUND, self.BACKGROUND_RECT)
            
            self.draw_keyboard()
            pygame.display.update()
            
            
