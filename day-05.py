str = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
str_left  = str.lstrip(",:%_#")

#isdisjoint()

def say_hi(name):
    '''
    This function return a string
    '''
    print(f'Hi {name}!')

#say_hi('Pablo')

def square(num):
    return num**2

def multiplication(num1, num2):
    return num1 * num2


# print(square(2))

res = multiplication(10, 100)

def check_3_digits(nums):
    for num in nums:
        if num in range(1, 1000):
            return True
        else:
            pass
    return False


# print(check_3_digits([5500, 9900, 7600,10000]))

coffe_prices = [('capuchino', 1.5), ('Expresso', 1.9), ('Moka', 1.5)]

def expensive_coffe(coffe_prices):
    prices  = [price for coffe, price in coffe_prices]
    exp_coffe = max(prices)
    for coffe, price in coffe_prices:
        if price == exp_coffe:
            return (coffe, price)
        else: 
            pass

# print(expensive_coffe(coffe_prices))


print('\n')
from random import *

def shuffle_sticks(sticks):
    shuffle(sticks)
    return sticks

def generate_sticks():
    sticks = [  (index, randint(1,100)) for index,num  in enumerate(range(1,5)) ]
    return shuffle_sticks(sticks)

def find_taller_stick(sticks):
   numbers = [num for index, num in sticks]
   taller_stick = max(numbers)
   for index, num,  in sticks:
       if num == taller_stick:
           return (index, num)

def pick_a_stick():
    sticks = generate_sticks()
    winner_stick = find_taller_stick(sticks)
    selected = 0

    while selected!=winner_stick[0]:
        selected = int(input('Select a number between 1 and 4: '))

    print(f'Stick {winner_stick} is the winner!\n {sticks}')

#pick_a_stick()


def lanzar_dados():
    resultado_dados = [ randint(1,6) for num in range(1, 3) ]
    # print(resultado_dados)
    return resultado_dados
    
dado_uno, dado_dos = lanzar_dados()
    
def evaluar_jugada(resultado_uno, resultado_dos):
    suma_dados = resultado_uno + resultado_dos
    if suma_dados <= 6:
        print(f'La suma de tus dados es {suma_dados}. Lamentable')
    elif suma_dados > 6 and suma_dados < 10:
        print(f'La suma de tus dados es {suma_dados}. Tienes buenas chances')
    else:
        print(f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora')

# evaluar_jugada(dado_uno, dado_dos)

lista_numeros = [1,2,15,7,2] 

def reducir_lista(lista_numeros):
    max_value = max(lista_numeros)
    lista_numeros.remove(max_value)
    return list(set(lista_numeros))

def promedio(lista_numeros):
    total_promedio = 0
    for numero in lista_numeros:
        total_promedio += numero
    return total_promedio / len(lista_numeros)
    
#print(promedio(reducir_lista(lista_numeros)))

def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    return choice(moneda)

def probar_suerte(moneda, lista_numeros):
    if moneda == 'Cara':
        print('La lista se autodestruirá')
        lista_numeros.clear()
        return lista_numeros
    elif moneda == 'Cruz':
        print('La lista fue salvada')
        return lista_numeros
    
# Unknowing args
    
def addition(a, b):
    return a+b
    
#print(addition(5,2))

def addition_with_args(*args):
    total = 0
    for arg in args:
        total+=arg
    return total

#print(addition_with_args(5,2,4,6,6,6))


# kwargs 

def addition_with_kargs(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f'{key} : {value}')
        total+=value
    return total

def addition_with_m_kargs(num1, num2, *args, **kwargs):
    total = 0
    print(f'\n First {num1} and second {num2} argument')
    print('\n*args')
    for arg in args:
        print(f'{arg}')
    print('\n**kargs')
    for key, value in kwargs.items():
        print(f'{key} = {value}')
        total+=value
    return total

args = [100, 200, 300]
kwargs = {'x': 10, 'y':2, 'z': 1 }

addition_with_m_kargs(10, 20,*args ,**kwargs)


# Practice 

def cantidad_atributos(**kwargs):
    total_llaves = 0
    for key, value in kwargs.items():
        total_llaves+=1
    return total_llaves    
    
kwargs = {
    'x': 1,
    'y':2,
    'z':3
}


def lista_atributos(**kwargs):
    la = [value for key, value in kwargs.items()]
    return la
    

kwargs= {
    'x':1, 
    'y':2,
    'z':3
}
    
print(lista_atributos(**kwargs))


def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f'{nombre_argumento}: {valor_argumento}')


#Exercise one
print('Exercise one')
def return_distinct(*c_args):
    total = 0
    for arg in c_args:
        total+=arg
    if total > 15:
        return max(args)
    elif total < 10:
        return min(args)
    else:
        return sum(args) / len(args)

    

c_args = [ 12, 13, 10 ]
print(return_distinct(*c_args))


def word_spliter(word):
    split = [ letter for letter in word ]
    unique_letters = list(set(split))
    unique_letters.sort()
    return unique_letters

print(word_spliter('entretenido'))



def zero_analizer(*z_args):
    for index, arg in enumerate(z_args):
        if index < len(z_args) - 1:
            print(f'{arg} == {z_args[index+1]} and {arg} == 0')
            if arg == z_args[index+1] and arg == 0:
                return True
            else:
                pass
    return False


#z_args = [5,6,1,0,0,9,3,5]
z_args = [6,0,5,1,0,3,0,1]
print(zero_analizer(*z_args))


def prime_number(number):
    primes=[]
    for i, n in enumerate(range(0, number)):
        if i!=0 and i!=1:
            if i%n==0 and i%2!=0:
                primes.append(i)
    return primes


print(prime_number(50))

# Hangman 

from random import *
print('\n')

rnd_words = ['happy','blue', 'dog', 'jump', 'apple', 'fast', 'bright', 'small', 'fun', 'rain']

def setup_player():
    player_name = input('What is your name? ')
    player = {
        'name': player_name,
        'turn': 0
    }
    print('Welcome to Hangam game ' + player['name'] + ' !' )
    return player

def split_word(word):
    splited_word = [letter.upper() for letter in word]
    return splited_word

def choice_rnd(elements):
    if type(elements)=='str':
        elements = [e.upper() for e in elements]
    return choice(elements)

def initialize_game():
    player = setup_player()
    word = split_word(choice_rnd(rnd_words))
    player_word = generate_player_word(word)

    while player['turn'] < 5:
        player_turn(word, player_word)
        if evaluate_end_game(word, player_word):
            print(f'\n Congratulation you guess the word {plain_word(word)}')
            break
        player['turn']+=1
    else:
        print('\n Sorry you have 0 turns left!')

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






