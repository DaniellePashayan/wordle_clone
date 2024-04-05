import pygame
import sys
import random
from src.settings import *
from src.Indicator import Indicator
from src.utility import get_word_list

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
        
        self.selected_word = self.select_random_word()

    def draw_keyboard(self):
        indicator_y = 550
        spacing_gap = 5
        # the keyboard rows are different sizes due to num of letters in each row
        # these numbers set the starting position of the letters in each row so that they are centered
        starting_indicator_x = [75, 95, 140]
        # renders the rows of the keyboard
        for i in range(len(KEYBOARD_ALPHABET)):
            # renders the letters in each row
            indicator_x = starting_indicator_x[i]
            for letter in KEYBOARD_ALPHABET[i]:
                new_ind = Indicator(indicator_x, indicator_y, letter, self.SCREEN)
                self.indicators.append(new_ind)

                # shifts the starting position of the letter on the x axis
                indicator_x += INDICATOR_SIZE_W + spacing_gap
                new_ind.draw()
            # shifts the position of the letter on the y axis for each new row and resets the x axis
            indicator_y += 55
    
    def select_random_word(self):
        # selects a random word from the list of words
        w = random.choice(get_word_list())
        print(w)
        return w
    
            
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
            pygame.display.flip()
            
            
