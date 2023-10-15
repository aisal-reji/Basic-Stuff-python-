# Character
char_variable = 'A'

# String
string_variable = 'Hello, World!'

# List
fruits = ['apple', 'banana', 'cherry']

# Dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Manipulating Character
char_variable = chr(ord(char_variable) + 1)
print(f"Manipulated Character: {char_variable}")

# Manipulating String
string_variable = string_variable.replace('Hello', 'Hi')
string_variable = string_variable.upper()
print(f"Manipulated String: {string_variable}")

# Manipulating List
fruits.append('date')
fruits.remove('cherry')
fruits.sort()
print(f"Manipulated List: {fruits}")

# Manipulating Dictionary
person['age'] = 31
person['country'] = 'USA'
del person['city']
print(f"Manipulated Dictionary: {person}")

