import pygame
import sys
import random
from src.settings import *
from src.indicator import Indicator
from src.utility import get_word_list

class Game:
    def __init__(self, SCREEN: pygame.Surface) -> None:
        self.SCREEN = SCREEN
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
        self.draw_keyboard()
    
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
    
    def draw_letter(self, key_pressed: str):
        # adds the letter to the current guess
        self.current_guess.append(key_pressed)
        self.current_guess_string += key_pressed
        self.current_letter_bg_x += 55
        # draws the letter on the screen
        new_letter = Indicator(self.current_letter_bg_x, 450, key_pressed, self.SCREEN)
        new_letter.draw()