import pygame
import sys
import random
from src.settings import *
from src.Indicator import Indicator
from src.utility import get_word_list
from src.Letter import Letter
from src.Window import Window

class Game:
    def __init__(self):
        self.SCREEN = Window().SCREEN
        self.count_of_guesses = 0

        # each guess is going to be a list of 5 letters
        # each time the user makes a guess, it will be iterated over and each guess will be displayed to the screen
        self.guesses = [[]] * 6

        # stores the current guess, with each letter being a part of the array
        self.current_guess = []
        # stores the current guess as a string
        self.current_guess_string = ""

        self.current_letter_bg_x = 110


        self.game_result = ""
        
        self.selected_word = self.select_random_word()
    
    def select_random_word(self):
        # selects a random word from the list of words
        return random.choice(get_word_list())
    
    def write_letter(self, key_pressed):
        self.current_guess_string += key_pressed
        new_letter = Letter(key_pressed, (self.current_letter_bg_x, self.count_of_guesses*100+LETTER_Y_SPACING))
        current_letter_bg_x += LETTER_X_SPACING
        self.guesses[self.guesses_count].append(new_letter)
        self.current_guess.append(new_letter)
        for guess in self.guesses:
            for letter in guess:
                letter.draw()
            
    def game_loop(self):
        w = Window()
        w.SCREEN.fill("white")
        w.SCREEN.blit(w.BACKGROUND, w.BACKGROUND_RECT)
        
        w.draw_keyboard()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                pygame.display.update()
            
            
