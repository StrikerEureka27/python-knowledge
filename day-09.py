from collections import Counter, defaultdict, namedtuple

numbers = [ 1, 2, 3, 4, 45, 5, 45, 45, 3, 5, 5 ]
phrase  = 'Al pan pan y al vino vino'
serie = Counter([1,1,1,1,1, 2,2,2,2,2, 3,3,3,3, 4,4,4,4,4,4,4])

print(Counter(numbers))
print(Counter(phrase.split()))
print(serie.most_common(1))

my_dic = defaultdict(lambda: 'none')

my_dic['one'] = 1
my_dic['two'] = 1

print(my_dic['three'])
print(my_dic)

Person = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Person('Ariel', 1.75, 80)

print(ariel.altura)

# os shutil module

import os
import shutil

print(os.getcwd())

file = open('text.txt', 'w')
file.write('Hello, how are you?')
file.close()

# print(os.listdir())

# Move a file

#shutil.move('course.txt', '/Users/pablocaceros/Documents/')

# Delete a empty folder
# os.rmdir('/Users/pablocaceros/Documents/')

# Delete directory files and subdirectories - warning this delete all without ask
# shutil.rmtree('/Users/pablocaceros/Documents/')

# pip install send2trash
#import send2trash

# send2trash.send2trash('text.txt')

print(os.walk('.'))

for route, sub, file in os.walk('.'):
    print(f'Route: {route}')
    for s in sub:
        print(f'Sub directories: {s}')
    print(f'Files: {file}')
    for f in file:
        if f.startswith('tets'):
            print(f'{f}')
        print(f'File : {f}')


print('\n')

import datetime

hour = datetime.time(17, 35)
date = datetime.datetime(1998, 8, 21)

today = date.today()
date = date.replace(month= 9)

print(hour)
print(date)
print(date.today())

life = today - date
print(life)

date2 = datetime.datetime.today().minute
print(date2)

import time

def test_for(number):
    list = []
    for n in range(1, number+1):
        list.append(n)
    return list

def test_while(number):
    list = []
    counter = 1
    while counter <= number:
        list.append(counter)
        counter+=1
    return list

start = time.time()
test_for(1500000)
end = time.time()

print(end - start)

start = time.time()
test_while(1500000)
end = time.time()

print(end - start)

import math


floor_res = math.floor(89.9833) # Round to the floor
ceil_res = math.ceil(89.9833) # Round to the top

print(floor_res)
print(ceil_res)

print(math.pi)

res_log = math.log(25, 5)
print(res_log)

# Regular expression

import re

text = 'Hi, call the number 555-555-5555 in case of a emergency number'

pattern = 'number'
res = re.search(pattern, text)
res2 = re.findall(pattern, text)

print(res.span())
print(res2)


