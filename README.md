# Python knowledge

Python is a high-level, general-purpose programming language known for its readability, simplicity, and versatility. It was created by Guido van Rossum and first released in 1991.

To start learning, there is no other way besides print a  `Hello world`, to achive this we can type:

```
print('Hello world')
```

## Data types

Table listing some of the commonly used data types in Python:

| Data Type     | Example               | Description                                       |
|---------------|-----------------------|---------------------------------------------------|
| int           | 42                    | Integer (whole number)                            |
| float         | 3.14                  | Floating-point number (decimal)                   |
| str           | 'Hello, World!'       | String (sequence of characters)                   |
| bool          | True or False         | Boolean (logical value)                          |
| list          | [1, 2, 'three']       | Ordered, mutable collection                       |
| tuple         | (1, 2, 'three')       | Ordered, immutable collection                     |
| set           | {1, 2, 3}             | Unordered collection of unique elements           |
| dict          | {'key': 'value'}      | Dictionary (key-value pairs)                      |
| complex       | 2 + 3j                | Complex number                                   |
| NoneType      | None                  | Represents the absence of a value                |
| bytes         | b'hello'              | Immutable sequence of bytes                      |
| bytearray     | bytearray(b'hello')   | Mutable sequence of bytes                         |
| range         | range(5)              | Represents a range of numbers                    |

If you want to see memory address yo can perfom:

```
print(hex(id(age)))
```

To print the type of a variable
```
type(variable_name)
```

Sometimes there ares several values that you need to print on screen there is differents ways to achive this

## String formats

Function format

```
print('My car color is {} and has a vehicle registration {}'.format(color, vehicleRegistration))
```
Literal chains

```
print(f'My car color is {color} and has a vehicle registration {vehicleRegistration}')
```

## Escape sequence

| Escape Sequence | Meaning                                      |
|------------------|----------------------------------------------|
| `\\`             | Backslash                                     |
| `\'`             | Single quote                                  |
| `\"`             | Double quote                                  |
| `\n`             | Newline (line break)                          |
| `\t`             | Tab                                          |
| `\r`             | Carriage return                               |
| `\b`             | Backspace                                     |
| `\f`             | Formfeed                                      |
| `\v`             | Vertical tab                                  |
| `\uXXXX`         | Unicode character with 16-bit hex value XXXX  |
| `\UXXXXXXXX`     | Unicode character with 32-bit hex value XXXXXXXX|
| `\N{name}`       | Unicode character named 'name'                |

## Operators

These are the basic operators to work with python

| Category               | Operators                                     |
|------------------------|-----------------------------------------------|
| Arithmetic Operators   | +, -, *, /, // (floor division), % (modulo)  |
| Comparison Operators   | ==, !=, <, >, <=, >=                          |
| Assignment Operators   | =, +=, -=, *=, /=, //=, %=                   |
| Logical Operators      | and, or, not                                  |
| Bitwise Operators      | &, |, ^, ~, <<, >>                            |
| Membership Operators   | in, not in                                   |
| Identity Operators     | is, is not                                   |

## String methods 

| Method                       | Description                                       |
|------------------------------|---------------------------------------------------|
| `len(str)`                   | Returns the length of the string.                 |
| `str.upper()`                | Converts all characters to uppercase.             |
| `str.lower()`                | Converts all characters to lowercase.             |
| `str.capitalize()`           | Converts the first character to uppercase.        |
| `str.title()`                | Converts the first character of each word to uppercase. |
| `str.startswith(prefix)`     | Checks if the string starts with a specified prefix.|
| `str.endswith(suffix)`       | Checks if the string ends with a specified suffix.  |
| `str.find(substring)`        | Returns the lowest index of the first occurrence of a substring.|
| `str.replace(old, new)`      | Replaces occurrences of a substring with another.  |
| `str.split(delimiter)`       | Splits the string into a list based on a delimiter.|
| `str.strip()`                | Removes leading and trailing whitespaces.          |
| `str.join(iterable)`         | Joins the elements of an iterable into a string using the string as a separator. |
| `str.isalpha()`, `str.isdigit()`, `str.isalnum()` | Checks if all characters are alphabetic, numeric, or alphanumeric. |
| `str.count(substring)`       | Returns the number of occurrences of a substring in the string. |

## Miscellaneous

Range: is a built-in function in Python that generates a sequence of numbers within a specified range. It is commonly used in for loops.

```
for i in range(5):
    print(i)
```
Enumerator: Is a built-in function in Python that adds a counter to an iterable, returning tuples containing the index and the corresponding element.

```
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value}")
```

Zip: Is a built-in function in Python that aggregates elements from two or more iterables (e.g., lists) and creates an iterator of tuples.

```
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]
zipped_data = zip(names, ages)
for name, age in zipped_data:
    print(f"Name: {name}, Age: {age}")
```

Max: Is a built-in function in Python that returns the largest item in an iterable or the largest of two or more arguments.

```
numbers = [3, 7, 2, 9, 5]
max_value = max(numbers)
print(f"The maximum value is: {max_value}")
```

Min: is a built-in function in Python that returns the smallest item in an iterable or the smallest of two or more arguments.

```
numbers = [3, 7, 2, 9, 5]
min_value = min(numbers)
print(f"The minimum value is: {min_value}")
```

List comprehension: is a concise way to create lists in Python. It provides a more readable and compact syntax for creating lists.

```
squares = [x**2 for x in range(5)]
print(squares)
```

## Function

A function is a block of code which only runs when it is called.

```
def say_hi(name):
    '''
    This function return a string
    '''
    print(f'Hi {name}!')
```

Args and kwargs

```
    def addition_with_args(*args):
        total = 0
        for arg in args:
            total+=arg
        return total

addition_with_args(5,2,4,6,6,6)

def addition_with_kargs(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f'{key} : {value}')
        total+=value
    return total

kwargs = {'x': 10, 'y':2, 'z': 1 }

```

## OOP (Object oriented programing)

Is a computer programming model that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.

- Encapsulation
- Inheritance
- Abstraction
- Polymorphism
