# OOP (Object oriented programing)
# Atributes [ instance | class ]

class Animal:

    def __init__(self, age, color):
        self.age = age
        self.color = color

    def born(self):
        print('This animal has born')
    
    def make_noise(self):
        print(f'''
        Animal and my color is {self.color}
        ''')

class Bird(Animal):

    wings = True 
    
    def __init__(self, age, color,  species):
        super().__init__(age, color) # inheritance atributes
        self.species = species

    def make_noise(self):
        print(f'''
        Pioo! and my color is {self.color}
        ''')

    def fly(self, distance):
        print(f'Bird fly {distance} meters')
        self.make_noise()

    @classmethod
    def lay_eggs(cls, quantity):
        print(f'Lay {quantity} eggs')

    @staticmethod
    def look():
        print('Bird look')

'''
Instance methods
Class methods @classmethod
Static methods @staticmethod
'''

my_bird = Bird(28, 'red', 'canary')
print(my_bird.color)
print(my_bird.species)

my_bird.make_noise()
my_bird.fly(40)

my_bird.wings = False
Bird.lay_eggs(10)
my_bird.wings = True

Bird.look()
print(my_bird.wings)
my_bird.born()

class Canary(Bird):
    pass


canary = Canary(21, 'green', 'canary')
canary.make_noise()

# inheritance

class Vehicle:

    def __init__(self, plate, color):
        self.plate = plate
        self.color = color
    
    def turn_on(self):
        print('Turn on vehicle')

class Car(Vehicle):

    def turn_on(self):
        print('Turn on car')


car = Car('23222', 'red')
car.turn_on()

my_list = [1,1,1,1,1]
print(len(my_list))

class Cd:

    def __init__(self, author, title, songs):
        self.author = author
        self.title = title
        self.songs = songs

    def __str__(self):
        return f'Album {self.title} of {self.author}'

    def __len__(self):
        return self.songs
    

cd  = Cd('Pink Floy', 'Nature', 21)
print(len(cd))

 

        