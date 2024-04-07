import pygame
import sys
import random
from src.settings import *
from src.indicator import Indicator
from src.utility import get_word_list, get_valid_english_words

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

        self.current_letter_bg_x = 25
        self.current_letter_bg_y = 65

        # a list that stores the Indicator objects. the indicator is placeholder that will represent each letter
        self.indicators = []

        self.game_result = ""
        
        self.selected_word = self.select_random_word()
        self.valid_words = get_valid_english_words()
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
                new_ind = Indicator(
                    x=indicator_x, 
                    y=indicator_y,
                    letter=letter,
                    screen=self.SCREEN,
                    width=KEYBOARD_SIZE_W,
                    height=KEYBOARD_SIZE_H, 
                    font_size=KEYBOARD_LETTER_SIZE)
                self.indicators.append(new_ind)

                # shifts the starting position of the letter on the x axis
                indicator_x += KEYBOARD_SIZE_W + spacing_gap
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
        self.current_guess_string += key_pressed
        self.current_letter_bg_x += GUESS_SIZE_W + 10
        current_y = self.current_letter_bg_y*(self.count_of_guesses+1)+(15*self.count_of_guesses)
        print(current_y)
        # draws the letter on the screen
        new_letter = Indicator(
            x = self.current_letter_bg_x, 
            y = current_y, 
            letter = key_pressed, 
            screen = self.SCREEN, 
            width = GUESS_SIZE_W,
            height = GUESS_SIZE_H, 
            outline=True,           
            bg_color=pygame.Color("white"),
            outline_color=pygame.Color("black"),
            font_size=60)
        self.guesses[self.count_of_guesses].append(new_letter)
        self.current_guess.append(new_letter)
        for guess in self.guesses:
            for letter in guess:
                letter.draw()
        
    def delete_letter(self):
        last_letter = self.guesses[self.count_of_guesses][-1]
        pygame.draw.rect(self.SCREEN, LIGHT_GRAY, last_letter.outline_dim)
        pygame.draw.rect(self.SCREEN, pygame.Color("white"), last_letter.bg_dim)
        # Remove the last letter from the current guess
        self.guesses[self.count_of_guesses].pop()
        self.current_guess_string = self.current_guess_string[:-1]
        self.current_guess.pop()
        self.current_letter_bg_x -= GUESS_SIZE_W + 10
        
    def check_guess_against_correct_word(self):
        # checks if the current guess is the same as the selected word
        # first checks if the entered word is in the word list
        if self.current_guess_string not in self.valid_words:
            print("Not a valid word")
        
        # if the word is correct, the game is won
        if self.current_guess_string == self.selected_word:
            self.game_result = "Win"
            game_completed = True
            # set all the letters to green
            for letter in self.current_guess:
                letter.bg_color = GREEN
                letter.text_color = pygame.Color("white")
                letter.outline = False
                letter.draw()
                self.game_result = "Win"
        else:
            if self.count_of_guesses < 6:
                for i in range(5):
                    letter = self.current_guess[i]
                    # check if letter is in set already
                    if self.current_guess_string[i] == self.selected_word[i]:
                        # if the letter is in the correct position, it will be green
                        letter.bg_color = GREEN
                        letter.text_color = pygame.Color("white")
                        letter.outline = False
                        print(f'{letter.letter} is green')
                    elif self.current_guess_string[i] in self.selected_word:
                        # if the letter is in the word but not in the correct position, it will be yellow
                        letter.bg_color = YELLOW
                        letter.text_color = pygame.Color("white")
                        letter.outline = False
                        print(f'{letter.letter} is yellow')
                    else:
                        self.current_guess[i].bg_color = DARK_GRAY
                        letter.text_color = pygame.Color("white")
                        self.current_guess[i].outline = False
                        print(f'{self.current_guess[i].letter} is grey')
                    letter.draw()
                pygame.display.update()
                self.count_of_guesses += 1
                self.current_guess = []
                self.current_guess_string = ""
                self.current_letter_bg_x = 25