# Day 4: 30 Days of python programming

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
space = ' '
e = a + space + b + space + space + c + space + d
print(e)

a = 'Coding'
b = 'For'
c = 'All'
d = a + space + b + space + c
print(d)
print()

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
first_word = company[0:6] # slices out first word
print(first_word)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_string = 'Coding' 
print(company.index(sub_string)) #returns the lowest index for the sub_string

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python')) # replaces the word Coding to Python

# Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace('All', 'Everyone')) # replaces the word All to Everyone

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split()) # splits the company string using space as the separator 

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(len(company) - 1)

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name .
company = 'Python For Everyone'
print(company[0] + company[7] + company[11])

# Create an acronym or an abbreviation for the name 'Coding For All'.
company = 'Coding For All'
print(company[0] + company[7] + company[11])

# Use index to determine the position of the first occurrence of C in Coding For All.
sub_string  = 'C'
print(company.index(sub_string))

# Use index to determine the position of the first occurrence of F in Coding For All.
sub_string2 = 'F'
print(company.index(sub_string2))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))

# Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
three_becuase= sentence[31:54]
print(three_becuase)

# Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
tab_sentence = '   Coding For All      '
print(tab_sentence.strip('  '))

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# Thirty_days_of_python
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'Thirty_days_of_python'
print(challenge.isidentifier())

# Use the new line escape sequence to separate the following sentences. I am enjoying this challenge. I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

"""
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
"""
radius = 10
area = 3.14 * radius ** 2
formated_string1 = 'The area of a circle with radius {} is {} meters square'.format(radius, area) # method 1
print(formated_string1)
formated_string2 = 'The area of a circle with radius %d is %d meters square' %(radius, area) # method 2
print(formated_string2)

"""
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
