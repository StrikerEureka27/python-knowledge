# Hangman 
from random import *
print('\n')

rnd_words = ['happy','blue', 'dog', 'jump', 'apple', 'fast', 'bright', 'small', 'fun', 'rain']

def setup_player():
    player_name = input('What is your name? ')
    print(f'Welcome to Hangam game {player_name}!' )

def split_word(word):
    splited_word = [letter.upper() for letter in word]
    return splited_word

def choice_rnd(elements):
    if type(elements)=='str':
        elements = [e.upper() for e in elements]
    return choice(elements)

def initialize_game():
    setup_player()
    word = split_word(choice_rnd(rnd_words))
    player_word = generate_player_word(word)
    turn = 0

    while turn < 5:
        player_turn(word, player_word)
        if evaluate_end_game(word, player_word):
            print(f'\n Congratulation you guess the word {plain_word(word)}')
            break
        turn+=1
    else:
        print('\n Sorry you have 0 turns left!')
        print(f'\n The word was {plain_word(word)}')

def player_turn(word, player_word):
        print(f'\n> {plain_word(player_word)} <\n')
        selected_letter = ask_for_letter()
        update_player_word(player_word, selected_letter, word)
        

def plain_word(player_word):
    return ''.join(player_word)

def update_player_word(player_word, selected_letter, word):
    for idx, letter in enumerate(word):
        if selected_letter == letter:
            player_word[idx] = letter
    return player_word

def generate_player_word(word):
    player_word = [ '_' for letter in word]
    rnd_letter = choice_rnd(plain_word(word))
    for idx, letter in enumerate(word):
        if letter == rnd_letter:
            player_word[idx] = letter
    return player_word

def evaluate_end_game(word, player_word):
    return plain_word(word)==plain_word(player_word)

def ask_for_letter():
    letter =  input('Type a letter ')
    if len(letter) == 1:
        return letter.upper()
    else:
        print('\n Sorry you enter a invalid letter')

initialize_game()