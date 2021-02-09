'''
Python data types
Numbers are integers and floating point
'''
i = 10
# i is integer (int)
j = 3.4

'''
Functions like int(), float(), str(), tuple(), list(), and dict()
exist to convert one type of object to another type
'''
k = int(j)
# k is an integer
m = float(i)
# m is a floating point number
big = 3.1e3
# j and big are floating point numbers (float)

'''
Strings can be quoted with single or double quotes
Balanced strings with three or more quotes are multi_line
'''
fname = "Keith "
lname = 'Wright'
# fname and lname are string
name = fname + ' ' + lname
age = 54
print (name + " " + str(age))
# string variable (str)

balanced = '''triple single'''
multi_line = '''401 Mile of Cars Way
National City, CA 91950'''
print(multi_line.upper())

'''
Boolean data types are True or False like alpha and beta
true values:
    True, 1, 'any', ['a'], ('one'), {'key':'value'}
false values:
    False, 0, 0.0, '', [], (), {}
boolean operators:
    and, or, not, ()
'''
alpha = True
beta = False
omega = not False
gamma = alpha or beta
delta = alpha and beta
lamda = 1 and not 1 or 1
zeta = 1 and not (1 or 1)
print("lamda", lamda)
print("zeta", zeta)

'''
Lists are objects separated by commas in square brackets [] and can be updated
'''
fruit = ['apple', 'pear', 'peach']
# list
fruit.extend((name, alpha, i, j))
print("Fruit list", fruit)

'''
Tuples are objects separated by commas in parentheses () and can NOT be updated
Conversion functions tuple() and list() can change from one type to the other
'''
colors = ('red', 'green', 'orange')
tfruit = tuple(fruit)
lcolors = list(colors)
# tuple

'''
Dictionaries are objects with keys associated with values
The different key and value pairs are separated by commas
and each key is separated by a colon from its value
'''
phones = {619:'San Diego South', 858: 'San Diego North'}
zipped = zip(colors, fruit)
# zip() pairs up each item in the first object as a key with one item in the second object as a value
fruitdict = dict(zipped)

print("Fruit dictionary", fruitdict)

