from random import randint

alphabet = 'ABCDEFGHIJKLMNOPQRSTWKYZ'
categories = {
    'C': 0,
    'P': 0,
    'F': 0
}

def generate_random_str():
    return f'{alphabet[randint(0, len(alphabet) - 1 )]}000{ randint(10, 100)}'

def ticket_decorator(fn_ticket):
    def decorator(category):
        print(f'\nWelcome, your turn is: \n')
        print(next(fn_ticket(category)))
        print(f'\nThanks for your patience\n')
    return decorator

@ticket_decorator
def generate_ticket(category):
    ticket_number = categories[category]
    while True:
        ticket_number+=1
        categories[category] = ticket_number
        complete_ticket_serial = f'{generate_random_str()}-{category}{ticket_number}'
        yield complete_ticket_serial



generate_ticket('C')
generate_ticket('P')
generate_ticket('F')
generate_ticket('F')
generate_ticket('P')
generate_ticket('C')
