
print('Hello day 02')

name = ''
#name = input('Tell me your name: ')
age = 25

print('Your name is: ' + name + ' ('+ hex(id(name)) +')')
#print(hex(id(name)))
#print(age)
#print(hex(id(age)))

# Integers and floats

calc = 10 + 100.2;

#print(type(calc));

# Conversions
# Implicit and explicit conversion

#age = input('Give your age: ')
print(age)

age = int(age)
print(type(age))

res = age + 100

print(type(res))
print(res)

# String format
color = 'red'
vehicleRegistration = 304056

# - function format 
print('My car color is {} and has a vehicle registration {}'.format(color, vehicleRegistration))

# - literal chains
print(f'My car color is {color} and has a vehicle registration {vehicleRegistration}')

x = 10
y = 15

print(f'Coord [{x},{y}]')

# Math operators

x = 6
y = 2

print(f'\nOriginal values x: {x} and y: {y}')
print(f'{x} + {y} es igual a {x+y}')
print(f'{x} - {y} es igual a {x-y}')
print(f'{x} * {y} es igual a {x*y}')
print(f'{x} / {y} es igual a {x/y}')

# Division at floor

print(f'{x} // {y} es igual a {x//y}')
print(f'{x} % {y} es igual a {x%y}')

print(f'{x} expo square {y} es igual a {x**y}')
print(f'{x} expo cube es igual a {x**3}')
print(f'{x} expo raiz es igual a {x**0.5}')

print(round(10.6555, 2));
print(round(10.455523232));
print(round(10.855523232));


sellerName = input('Type your name: ')
salesAmount = input('Type your total sales: ')

salesAmount = float(salesAmount)
totalAmount = round((salesAmount * 13) / 100, 2)

print(f'\nHey! {sellerName}\n, your total comissions are ${totalAmount}')

