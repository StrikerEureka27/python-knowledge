import os
from os import system
from pathlib import Path

def initialize_recipe_book():
    print('\n' + '*'*39 +'\n')
    welcome()
    print('\n' + '*'*39)
    press_any_key()
    recipe_menu()

def get_dir_name(path):
     dirname = os.path.basename(path)
     return dirname

def setup_recipies_repo():
    crnt_wd = os.getcwd()
    dirname = get_dir_name(crnt_wd)
    project_path = Path(crnt_wd, 'projects', 'recipe_book')
    short_part = Path(dirname,'projects', 'recipe_book')
    return project_path, short_part

def list_recipies_in_path(path):
    recipies = [rec for rec in Path(path).glob('**/*.txt')]
    return recipies

def list_categories_in_path(path):
    categories = [file.name for file in Path(path).iterdir() if file.is_dir()]
    return categories

def count_recipies(path):
    recipies_counter = [ rec for rec in Path(path).glob('**/*.txt') ] 
    return len(recipies_counter)

def welcome():
    
    project_path, short_path = setup_recipies_repo()
    recipies_counter = count_recipies(project_path)

    print(f'\tWelcome to recipe book')
    print(f'\tYour recipies are in \n {short_path}')
    print(f'\tYou have {recipies_counter} recipies')

def press_any_key():
    enter =  input('\n Press enter to continue... ')
    if enter!=None:
        system('clear')
    
def recipe_menu():
    option = 0

    while(option!=6):
        print('\n'+'*'*10 + '\tMenu\t' + '*'*10+'\n')
        print(f' [ 1 ] Read recipie ')
        print(f' [ 2 ] Create recipie ')
        print(f' [ 3 ] Create category ')
        print(f' [ 4 ] Delete recipie ')
        print(f' [ 5 ] Delete category ')
        print(f' [ 6 ] Exit ')
        print('\n'+'*'*34 +'\n')
        
        option =  int(input('\nSelect a option: '))

        match option:
            case 1:
                chose_category('read')
            case 2:
                chose_category('create')
            case 3:
                chose_category('create_category')
            case 4:
                delete_recepie()
            case _:
                print('Invalid option')
            
def chose_category(action_type):
    clean_screen()
    print('\n' + '*'*39 +'\n')
    project_path, short_path = setup_recipies_repo()
    categories  = list_categories_in_path(project_path)
    for idx, category in enumerate(categories):
        print(f' [ {idx} ] {category} ')
    
    print('\n' + '*'*39 +'\n')

    if action_type!='create_category':
        selected_category = int(input('Select a category: '))
        category_path = category_path_generator(categories[selected_category])
        category_name = categories[selected_category]

    match action_type:
        case 'read':
            chose_recipies(category_name)
        case 'create':
            create_recipie(category_path)
        case 'create_category':
            create_category()

def create_recipie(recipe_path):
    recipe_name = input('Enter the new recepie name: ')    
    recipe_content = input('Enter the recepie content: ')
    recipe_path = f'{recipe_path}/{recipe_name}.txt'
    file = open(recipe_path, 'w')
    file.write(recipe_content)
    file.close()

def create_category():
    project_path, short_path = setup_recipies_repo()
    category_name = input('Enter the name of the new category: ') 
    os.makedirs(f'{project_path}/{category_name}')

def delete_recepie():
    project_path, short_path = setup_recipies_repo()
    print('\n' + '*'*39 +'\n')
    recipies = list_recipies_in_path(project_path)
    for idx, rec in enumerate(recipies):
        print(f'[ {idx} ] {rec.stem}')
    print('\n' + '*'*39 +'\n')

    selected_recipie = int(input('Select a recipe: '))
    os.remove(recipies[selected_recipie])


def category_path_generator(selected_category_name):
    project_path, short_path = setup_recipies_repo()
    category_path = Path(project_path, selected_category_name)
    return category_path

def chose_recipies(selected_category_name):
    clean_screen()
    print('\n' + '*'*39 +'\n')
    print(f'{selected_category_name.upper()} category selected \n')
    category_path = category_path_generator(selected_category_name)
    recipies = list_recipies_in_path(category_path)
    for idx, rec in enumerate(recipies):
        print(f'[ {idx} ]  {rec.stem}')
    print('\n' + '*'*39 +'\n')

    selected_recipie = int(input('\nSelect a recipie: '))
    selected_recipie_name = recipies[selected_recipie]
    read_recipie(category_path, selected_recipie_name)

def read_recipie(category_path, recipe_name):
    print(f'\n{recipe_name.stem} selected')
    path = f'{category_path}/{recipe_name.stem}.txt'
    file = open(path, 'r')
    print(file.read())
    file.close()
    press_any_key()
   
def clean_screen():
    system('clear')

initialize_recipe_book()
   