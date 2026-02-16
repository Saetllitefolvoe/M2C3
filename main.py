# M2C3 Assigment 

#Exercise 1

string = 'Juncal'
number = 37 
list = ['Juncal', 'Josu', 'Olga']
my_boolean = True

# Exercise 2

palabra = 'Juncal'
primeras_tres = palabra[0:3]

# Exercise 3

list = ['Juncal', 'Josu', 'Olga']
primera_palabra = list[0]

# Exercise 4 

number = 10
var_num_sum = number + 10

# Exercise 5

list = ['Juncal', 'Josu', 'Olga']
ultima = list[-1]

# Exercise 6

names = 'harry,alex,susie,jared,gail,conner'
my_split = names.rsplit(',')

# Exercise 7

juncal = "tiene el pelo largo y oscuro"

""" Prueba 1
jun_ind = juncal.index(" ")
primera_palabra = juncal[:jun_ind]
upper_primera_palabra = primera_palabra.upper()
"""
"""" Prueba 2
jun_ind = juncal[:juncal.index(" ")].upper()
"""
jun_ind = juncal.split()[0].upper()

# Exercise 8 

name = 'Juncal'
pets = 2
pets_name = 'Josu and Olga'

greet ="Hi {0}, your {1} pets, {2}, have already have lunch today".format(name, pets, pets_name)

#Exercise 9

print("Hello world")

#Checkpoint 3 Exercise 

my_str = 'Hola, gracias por su compra'
query = my_str.find('Hola')
my_str = my_str.replace('Hola', 'Adios')

print(my_str)

