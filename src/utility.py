# get all the words from https://www.wordunscrambler.net/word-list/wordle-word-list

import requests
from bs4 import BeautifulSoup
import re

def get_word_list():
    url = "https://www.wordunscrambler.net/word-list/wordle-word-list"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    word_list = soup.find_all('a', href=re.compile("/unscramble/"))
    return [word.get_text().upper() for word in word_list]

def write_word_list_to_file(word_list):
    with open("word_list.txt", "w") as file:
        for word in word_list:
            file.write(word + "\n")

def get_word_list_from_file():
    with open("word_list.txt", "r") as file:
        return file.read().splitlines()

if __name__ == "__main__":
    word_list = get_word_list()
    write_word_list_to_file(word_list)