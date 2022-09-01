# Day 3: 30 Days of python programming
"""
Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
"""
import math

age = 30
height = 1.55
point = 1 + 4j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input('Enter base of triangle: '))
height = int(input('Enter height of triangle: '))
area = 0.5 * base * height
print('Area of triangle: ', area)
print()

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print('Perimeter of triangle: ', perimeter)
print()

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter length: '))
width = int(input('Enter width: '))
area = length * width
print('Area of rectangle: ', area)
perimeter = 2 * (length + width)
print('Perimeter of rectangle', perimeter)
print()

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = int(input('Enter radius: '))
area_circle = pi * radius ** 2
print('Area of circle: ', area_circle)
circumference_circle = 2 * pi * radius
print('Circumference of circle: ', circumference_circle)
print()

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope1 = 2 # y = mx + c where m = slope
print('slope1: ', slope1)
yintercept1 = -2 # c1 = y-intercept
print('y-intercept1: ', yintercept1)
# x intercept is when y = 0
# 2x - 2 = 0
xintercept1 = 2/2
print('x-intercept1: ', xintercept1)
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope2 = (10-2)/(6-2) # where m2 = slope
print('slope2: ', slope2)
# Euclidean distance = √[(x2 – x1)2 + (y2 – y1)2].
x_diff_squared = (6-2) ** 2
y_diff_squared = (10-2) ** 2
euclidean_distance = math.sqrt(x_diff_squared + y_diff_squared)
print('Euclidean distance: ', euclidean_distance)
# Compare the slopes in tasks 8 and 9.
print('slope1 > slope2', slope1 > slope2)
print()

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = 2
y = x^2 + 6*x + 9
print('the value of y: ', y)
print()

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = print(len('python'))
dragon_length = print(len('dragon'))
print('python_length != dragon_length', python_length != dragon_length)
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on in python and on in dragon', 'on' in 'python' and 'on' in 'dragon')
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon in I hope this course is not full of jargon', 'jargon' in 'I hope this course is not full of jargon')
# There is no 'on' in both dragon and python
print('There is no on in both dragon and python', 'on' is not 'python' and 'dragon')

# Find the length of the text python and convert the value to float and convert it to string
python_length = float(len('python'))
print(python_length)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x = 4 # even number
print('x is even because x % 2 == 0 ', x % 2 == 0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)
print()

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter hours: '))
hourly_rate = int(input('Enter hourly rate: '))
weekly_pay = hours * hourly_rate
print('Your weekly earning is ', weekly_pay)

"""
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
"""
a = '''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
print(a)


