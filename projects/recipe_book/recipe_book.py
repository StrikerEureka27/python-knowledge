import os
from os import system
from pathlib import Path

def initialize_recipe_book():
    project_path, short_path = setup_recipies_repo()
    recipies_counter = count_recipies(project_path)

    footer_count  = print_decoration_title(' Welcome to recipe book ', 5)
    print(f'''
    Your recipies are in 
    > {short_path} <
    and you have {recipies_counter} recipies.
    ''')
    print_decoration_footer(footer_count)
    press_any_key()

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

def press_any_key():
    enter =  input('\n Press enter to continue... ')
    if enter!=None:
        system('clear')
        recipe_menu()

def print_decoration_title(title, size):
    message = '*'*size + title + '*'*size
    print('\n'+message+'\n')
    return len(message)

def print_decoration_footer(size):
    return print('\n'+'*'*size + '\n')    

def recipe_menu():
    menu_option = ''
    while(menu_option!='6'):
        footer_counter = print_decoration_title(' Menu ', 15)
        print(''' 
         [ 1 ] List recipies. 
         [ 2 ] Create recipie.
         [ 3 ] Create category. 
         [ 4 ] Delete recipie.
         [ 5 ] Delete category. 
         [ 6 ] Exit.
        ''')
        print_decoration_footer(footer_counter)
        
        while not menu_option.isnumeric() or int(menu_option) not in range(1, 7):
            menu_option = input('\nSelect a option: ')

        match menu_option:
            case '1':
                chose_category('list')
            case '2':
                chose_category('create')
            case '3':
                chose_category('create_category')
            case '4':
                chose_recipie('','delete')
            case '5':
                chose_category('delete_category')
            case _:
                print('Invalid option')

def chose_category(action_type):
    clean_screen()
    foot_counter = print_decoration_title(f' {action_type} categories ', 15)     
    project_path, short_path = setup_recipies_repo()
    categories  = list_categories_in_path(project_path)
    for idx, category in enumerate(categories):
        print(f' [ {idx} ] {category} ')
    print_decoration_footer(foot_counter)

    if action_type!='create_category':
        selected_category = int(input('Select a category: '))
        category_path = category_path_generator(categories[selected_category])
        category_name = categories[selected_category]

    match action_type:
        case 'list':
            chose_recipie(category_name, 'read')
        case 'create':
            create_recipie(category_path)
        case 'create_category':
            create_category()
        case 'delete_category':
            delete_category(category_name)

def chose_recipie(selected_category_name, action_type):
    clean_screen()
    foot_counter = print_decoration_title(f' {action_type} recipies ', 15)     
    if selected_category_name != '':
        print(f'{selected_category_name.upper()} category selected \n')
    category_path = category_path_generator(selected_category_name)
    recipies = list_recipies_in_path(category_path)
    for idx, rec in enumerate(recipies):
        print(f'[ {idx} ]  {rec.stem}')
    print_decoration_footer(foot_counter)

    selected_recipie = int(input('\nSelect a recipie: '))
    selected_recipie_name = recipies[selected_recipie]

    match action_type:
        case 'read':
            read_recipie(category_path, selected_recipie_name)
        case 'delete':
            delete_recepie(selected_recipie_name)

def create_recipie(recipe_path):
    recipe_name = input('Enter the new recepie name: ')    
    recipe_content = input('Enter the recepie content: ')
    recipe_path = f'{recipe_path}/{recipe_name}.txt'
    file = open(recipe_path, 'w')
    file.write(recipe_content)
    file.close()
    press_any_key()

def delete_recepie(selected_recipie_name):
    os.remove(selected_recipie_name)
    press_any_key()

def create_category():
    project_path, short_path = setup_recipies_repo()
    category_name = input('Enter the name of the new category: ') 
    os.makedirs(f'{project_path}/{category_name}')
    press_any_key()

def delete_category(category_name):
    os.rmdir(category_path_generator(category_name))
    press_any_key()

def category_path_generator(selected_category_name):
    project_path, short_path = setup_recipies_repo()
    category_path = Path(project_path, selected_category_name)
    return category_path

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