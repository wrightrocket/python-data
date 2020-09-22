''' python data types '''
i = 10
# i is integer (int)
j = 3.4

k = int(j)
m = float(i)

big = 3.1e3
# j and big are floating point (float)

name = "Keith "
lname = 'Wright'
balanced = '''triple single'''

age = 54
print (name + str(age))
# string variable (str)

alpha = True
beta = False
'''
true things:
    True, 1, 'any', ['a'], ('one'), {'key':'value'}
false objects
    False, 0, 0.0, '', [], (), {}
'''
# boolean

fruit = ['apple', 'pear', 'peach']

# list

colors = ('red', 'green', 'orange')
tfruit = tuple(fruit)
lcolors = list(colors)
# tuple

phones = {619:'San Diego South', 858: 'San Diego North'}
zipped = zip(colors, fruit)
fruitdict = dict(zipped)

print(fruitdict)

# dictionary
