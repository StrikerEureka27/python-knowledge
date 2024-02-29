# Logic operators

my_value = 10!=2

# print(my_value)
print(hex(id(my_value)))


a = 10
b = 2
c = 15


my_value = 10>=2 and 15>=10 
my_value = 10>=2 or 15>=10 

txt = 'This is a short phrase'

my_value = 'phrase' in txt
my_value = not('phrase' in txt)

print(my_value)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = not(palabra1 in frase or palabra2 in frase)

# Flow control

if 'algooo' in frase:
    print('Es correcto')
elif 'algooo' in frase:
    print('"Algo" word found')
elif 'suficientementeg' in frase:
    print('Suficientemente word found')
elif 'no le' in frase:
    print('No word found')
elif 'el' in frase:
    print('El word found')
else:
    print('No result found')

ratings = 10

if ratings >=7:
    print('You are over the ratings')
    if ratings == 7:
        print('3rd prize!')
    elif ratings > 7 and ratings <= 9:
        print('2nd prize!')
    else:
        print('1st prize')
else:
    print('Your note is under the spectations')


edad = 16
tiene_licencia = False

if edad >= 18:
    if tiene_licencia:
        print('Puedes conducir')
    else:
        print('No puedes conducir. Necesitas contar con una licencia')
else:
    print('No puedes conducir aún. Debes tener 18 años y contar con una licencia')

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif not(habla_ingles):
    print("Para postularte, necesitas tener conocimientos de inglés")
elif not(sabe_python):
    print("Para postularte, necesitas saber programar en Python")
else:
    print('Para postularte, necesitas saber programar en Python y tener conocimientos de inglés')


# Loops
print('\n')
people  = [ 'Juan', 'Maria', 'Carlos', 'Belen' ]

for person in people:
    index = people.index(person)
    if person=='Maria':
        people[index] = person.upper()
    else:
        people[index] = person.lower()

    print(f'({index}) Hello {person}!')

print(people)

print('\n')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    index = numbers.index(num)
    if index > 0:
        for num in numbers:
            print(f' {num} x {index}  = { num * index }')
    print('\n')  

str = 'Hello world!'

for s in str:
    print(s)

print('\n')
nested_numbers  = [ [1, 2], [3, 4], [5, 6] ]

for numbers in nested_numbers:
    for num in numbers:
        print(num)
    print(numbers)

print('\n')
for x, y in nested_numbers:
    print(f' > {x} , {y} <')

print('\n')
dic = { 'c1':'a', 'c2':'b', 'c3':'c' }
for key, value in dic.items():
    print(f'{key} : {value}')


# While loop
    
coins = 5

while coins<100:
    coins+=1
    print(f'Coin: {coins}')
else: print('Se llego al final del loop')
    
print(f'Total coins: {coins}')

option = 'n'

while option != 'n':
    option = input('Continue? (n/y): ')
else: print('Thanks for your visit')

# Range

for num in range(5):
    print(num)

for num in range(2,5):
    print(num)

for num in range(1,100, 5):
    print(num)

listr = list(range(1,100))

print(listr)
 
alphabet = ['a', 'b', 'c']
index = 0

for letter in alphabet:
    print(f'{index} : {letter}')
    index+=1

for index, letter in enumerate(alphabet):
    print(f'{index}   {letter}')

# ZIP
    
names = ['Ana', 'Hugo', 'Valeria']
ages = [18, 20, 30]
cities = ['Lima', 'Madrid', 'Mexico']

combined = list(zip(names, ages, cities))
print(combined)

for name, age, city in combined:
    print(f'My name is  {name}\n I\'m {age} years old,\n and I\'m from {city}')


diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())

for nombre, edad in diccionario_edades.items():
    diccionario_edades[nombre] = nombre.lower()

ultimo_nombre = max(diccionario_edades.keys())
print(ultimo_nombre)

# Random

from random import *

rnd = randint(1, 50)
print(rnd)

unf = uniform(1, 5)
print(round(unf,2))

rnd = random()
print(rnd)

colors = ['blue', 'yellow', 'red', 'black']
rnd_color = choice(colors)
print(rnd_color)

shuffle(colors)
print(colors)


# List by compretion

word = 'Hello'
chain  = [letter for letter in word if letter != 'H']
chain2  = [letter if letter != 'H' else 'A' for letter in word]
print(chain)
print(chain2)

feets = [10, 20, 30, 40]
meters  = [ round(feet / 3.28, 2) for feet in feets ]

print(meters)

# Match

serie = 'N2-02'

if serie == 'N1-01':
    print('samsung')
elif serie == 'N2-02':
    print('Nokia')
elif serie =='N3-03':
    print('Motorola')

match serie:
    case 'N1-01':
        print('samsung')
    case 'N2-02':
        print('Nokia')
    case 'N3-03':
        print('Motorola')    




    
