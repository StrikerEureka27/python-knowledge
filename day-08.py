'''
    This moddule print a value
'''

# Error handler

def addition(a, b):
    return a + b

#a  = input('Enter a value: ')


try:
    addition(1, 20)
except TypeError:
    print('Error, you are trying to concatenate diferent types')
except ValueError:
    print('This is a invalid number')
else:
    print('Thanks, for using our services')
finally:
    print('End of the operation')


def ask_for_a_value():
    while True:
        try:
            value = int(input('Enter a number: '))
        except:
            print('That\'s is not a number')
        else:
            print(f'You enter the value {value}')
            break


# ask_for_a_value()

#Pylint

number1 = 10
#print(Number1)
# pylint day-08.py -r y

#Unit test

# Decorators
def change_text(type):

    def make_upper(text):
        print(text.upper())

    def make_lower(text):
        print(text.lower())

    if type == 'upper':
        return make_upper
    elif type == 'lower':
        return make_lower

some_change_text_function =  change_text('upper')
some_change_text_function('Python')


def decoration_change_text(make_a_change_function):
    def decoration(word):
        print('head')
        make_a_change_function(word)
        print('foot')
    return decoration

@decoration_change_text
def make_upper_2(text):
        print(text.upper())

@decoration_change_text
def make_lower_2(text):
        print(text.lower())

make_lower_2('HELLO WORLD')
make_upper_2('hello BEE')

# Generators

def number_generator():
    yield 4

g = number_generator()
print(next(g))

def list_number_generator():
    for n in range(1, 5):
        yield n * 10


lg  = list_number_generator()

print(next(lg))
print(next(lg))
print(next(lg))
print(next(lg))

def infinite_number_generator():
    num = 1
    yield num
    
    while num !=0:
        num +=1
        yield num
  

generador = infinite_number_generator()
    
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

def multiple_of_seven():
    counter = 1
    num = 7
    yield num
 
    while num!=0:
         counter +=1
         yield num * counter

generador = multiple_of_seven()

def subtract_live():
    lives = 4
    
    while lives !=0:
        lives -=1
        if lives > 1:
            yield print(f'Te quedan {lives} vidas')
        elif lives == 0:
            yield print('Game Over')
            break
        else:
            yield print(f'Te queda {lives} vida')
    
 
perder_vida = subtract_live()

next(perder_vida)
next(perder_vida)
next(perder_vida)
next(perder_vida)