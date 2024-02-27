from os import system
from random import *

class Person:
    def __init__(self, name, last_name):
        self.name =  name
        self.last_name = last_name

class Client(Person):

    balance = 0

    def __init__(self, name, last_name, numero_cuenta):
        super().__init__(name, last_name)
        self.numero_cuenta = numero_cuenta
    
    def deposit(self, amount):
        self.balance +=amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -=amount
        else:
            print('Insufficient funds')

def ask_for_amount():
    amount = int(input('Enter the amount: '))
    return amount

def press_any_key():
    enter =  input('\n Press enter to continue... ')
    if enter!=None:
        system('clear')

def clean_screen():
    system('clear')

def print_decoration_title(title, size):
    message = '*'*size + title + '*'*size
    print('\n'+message+'\n')
    return len(message)

def print_decoration_footer(size):
    return print('\n'+'*'*size + '\n')  

def create_client():
    footer_count = print_decoration_title(' Create client ', 15)
    client_name = input('Enter your name: ') 
    last_name = input('Enter your last name: ') 
    print_decoration_footer(footer_count)
    bank_account  = f'{client_name[0:2].upper()}000{randint(0, 100)}'
    print(client_name, last_name, bank_account)
    client = Client(client_name, last_name, bank_account)
    return client

def bank_menu(client):
    option = 0
    clean_screen()
    footer_count = print_decoration_title(' Bank managment ', 15)
    print(f'Balance : {client.balance}')
    while option<=3:
        print(f'''
        [ 1 ] Deposit.
        [ 2 ] Withdraw.
        [ 3 ] Exit.
    ''')
        print_decoration_footer(footer_count)
        option = int(input('Select a option: '))
        match option:
            case 1:
                clean_screen()
                client.deposit(ask_for_amount())
                press_any_key()
                bank_menu(client)
            case 2:
                clean_screen()
                client.withdraw(ask_for_amount())
                press_any_key()
                bank_menu(client)
                

def initialize_bank():
    client = create_client()
    bank_menu(client)


initialize_bank()