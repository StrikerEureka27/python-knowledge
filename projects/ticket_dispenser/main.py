'''
    Cosmetics
    Pharmacy
    Perfumery
'''

from os import system
import numbers

def press_any_key():
    enter =  input('\n Press enter to continue... ')
    if enter!=None:
        system('clear')

def initialize_ticket_machine():
    system('clear')
    store_selected = 0
    while store_selected!=4:
        print('''
        Welcome to the mall
        [ 1 ]  Cosmetics
        [ 2 ]  Pharmacy
        [ 3 ]  Perfumery
        [ 4 ]  Exit
    ''')
        
        try:
            store_selected = int(input('\n Please select a store, to generate a ticket: '))
        except:
            print('\nYou enter a invalid character')
            press_any_key()
            initialize_ticket_machine()

        match store_selected:
            case 1:
                system('clear')
                numbers.generate_ticket('C')
            case 2:
                system('clear')
                numbers.generate_ticket('P')
            case 3:
                system('clear')
                numbers.generate_ticket('F')

        press_any_key()


initialize_ticket_machine()
