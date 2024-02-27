# Files manipulation (I/O)

# Input

# my_file = open('hello.txt')

# print(my_file.read())
# first_line = my_file.readline()

'''for line in my_file:
    print(line.rstrip())'''

'''all_text = my_file.readlines()'''


# Output

'''
r: read only
w: write only
a: only write at the end
'''

my_file = open('hello_write.txt', 'a')

my_file.write('I\'m the new text\n')
my_file.write('I\'m the new line\n')

my_file.write('''
This is a new line
This is the 2nd line
This is the third line
''')

my_file.writelines(['Hello\t', 'word\n'])


my_file.close()


import os

# get current working directory
path = os.getcwd()
print(path)

# File path
# os.chdir('/Users/pablocaceros/Documents/')

my_text = open('text.txt','w')
my_text.write('Hello word, from text')
my_text.close()
my_text = open('text.txt','r')
print(my_text.read())

my_text.close()

# Create file
#os.makedirs('/Users/pablocaceros/Documents/files')

# basename and dirname

basename = os.path.basename(path)
dirname = os.path.dirname(path)
dirname = os.path.split(path)
split_path = os.path.split(path)

print(split_path)
print(f' basename: {basename} and dirname: {dirname}')

# Remove directory

#os.rmdir('/Users/pablocaceros/Documents/files')

from pathlib import Path

dir = Path('/Users/pablocaceros/Documents/python/python-knowledge/files')

al_file  = dir / 'alt_text.txt'
my_alt_file = open(al_file, 'r')
print(my_alt_file.read())
print(al_file.suffix)
print(al_file.stem)

if not al_file.exists():
    print('This file dosen\'t exist')
else:
    print('This file exists')

my_alt_file.close()


current_path = os.getcwd()
base = Path.home()

alt_2_path = Path(current_path, "alt_files", "hello_alt.txt")
alt_3_path = alt_2_path.with_name('new_name.txt')

'''
print(alt_2_path)
print(alt_2_path.parent) # cd ..
print(alt_3_path)
'''
# See for all txt
# one directory 
for txt in Path(current_path).glob('*.txt'):
    print(txt)

# with subdirectories

for txt in Path(current_path).glob('**/*.txt'):
    print(txt)    

# is realative to

print('\n')
alt_4_path = Path('Europe', 'Spain','madrid', 'text.txt')

in_spain = alt_4_path.relative_to(Path('Europe') , 'Spain')
print(alt_4_path)
print(f'in spain: {in_spain}')

'''
from os import system
system('clear')
'''
