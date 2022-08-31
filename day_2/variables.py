# Day 2: 30 Days of python programming
"""
Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line
"""
import math

first_name = 'Paul'
last_name = 'Jin'
full_name = 'Paul Jin'
country = 'America'
city = 'Severn'
age = 30
year = '2022'
is_married = False
is_true = True
is_light_on = True
x, y, z = 2, 4, 8
print()

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(z))

#Using the len() built-in function, find the length of your first name
print(len(first_name))
print(len(last_name))

"""
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
"""
num_one, num_two = 5, 4
total = print('total: ', num_one + num_two)
diff = print('diff: ', num_two - num_one)
product = print('product: ', num_two * num_one)
division = print('division: ', num_one / num_two)
remainder = print('remainder: ', num_two % num_one)
exp = print('exp: ', num_one ** num_two)
floor_division = print('floor division: ', num_one // num_two)

# The radius of a circle is 30 meters
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30 
area_of_circle = print('area of circle: ', math.pi * radius ** 2)

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = print('circumference of circle: ', 2 * math.pi * radius)

# Take radius as user input and calculate the area.
user_radius = input('Enter radius: ') # takes user input 
area_of_circle2 = print('area of circle: ', math.pi * int(user_radius) ** 2)
print()

# Use the built-in input function to get first name, last name, country and age from a user and 
# store the value to their corresponding variable names
first_name = input('Enter first name: ') # takes user first name
last_name = input('Enter last name: ') # takes user last name
country = input('Enter country: ')
age = input('Enter age: ')
print()

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')