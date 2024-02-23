# Python knowledge

Python is a high-level, general-purpose programming language known for its readability, simplicity, and versatility. It was created by Guido van Rossum and first released in 1991.

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


