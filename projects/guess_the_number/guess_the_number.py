from random import *

tries = 8
rnd_num = randint(0, 100)
#print(rnd_num)


player_name  = print('Welcome! ' +input('Give me a name: ') + '\n I\'m thinking in a number between 1 and 100, \n you have to guess the number!')

while tries <= 8:
    player_num = int(input(f' {tries} oportunities to guess: '))
    if player_num not in range(1, 101):
        print(f'Number {player_num} it\'s out of the allowed range')
    elif player_num < rnd_num:
        print(f'{player_num} is below the number')
    elif player_num > rnd_num:
        print(f'{player_num} is over the number')
    elif player_num == rnd_num:
        print(f'Congratulation you guess the number {rnd_num} at {abs(tries-8)} tries!')
        break
    else:
        print('Something go wrong, please restart the game')
    tries -= 1
    print(f'Sorry, you have {tries} tries left')