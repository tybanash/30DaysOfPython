# Day 5: 30 Days of python programming

# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
cities = ['Oshawa', 'Whitby', 'Ajax', 'Pickering']

# Find the length of your list
print(len(cities))

# Get the first item, the middle item and the last item of the list
print(cities[0])
first_middle = int(len(cities) / 2) - 1 # first middle because length of list is even
second_middle = int(len(cities) / 2) # second middle
print(cities[first_middle], ',', cities[second_middle])
last_index = len(cities)-1
print(cities[last_index])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Nadege', 25, 1.55, 'single', 'Canada']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
last_index = len(it_companies)-1
print(it_companies[last_index])

# Print the list after modifying one of the companies
it_companies[4] = 'Netflix'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Salesforce')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Shopify')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())

# Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))

# Check if a certain company exists in the it_companies list.
does_exist = 'Amazon' in it_companies
print(does_exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[0:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
print(it_companies[4:5])

# Remove the first IT company from the list
it_companies.remove('Shopify')
print(it_companies)

# Remove the middle IT company or companies from the list
del it_companies[3:5] # using del because it removes multiple items
print(it_companies)

# Remove the last IT company from the list
it_companies.pop(len(it_companies)-1)
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack1 = front_end + back_end
print(full_stack1)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = full_stack1.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)
print()

# The following is a list of 10 students ages: ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort
print(ages)
min_age = min(ages)
print(min_age)
max_age = max(ages)
print(max_age)

# Add the min age and the max age again to the list
ages.insert(len(ages)+1, min_age)
ages.insert(len(ages)+1, max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
median_age = (ages[5] + ages[6]) / 2
print(median_age)

# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(average_age)

# Find the range of the ages (max minus min)
range_age = max_age - min_age
print(range_age)

# Compare the value of (min - average) and (max - average), use abs() method
min_average = abs(min_age - average_age)
print(min_average)
max_average = max_age - average_age
print(max_average)
print(min_average == max_average)

# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
middle_country = int(len(countries) / 2)
print(countries[middle_country])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_list = countries[0:int(len(countries)/2)]
print(first_list)
print()
second_list = countries[int(len(countries)/2) :]
print(second_list)
print()

# or using unpacking method
first, second = [countries[0:int(len(countries)/2)], countries[int(len(countries)/2) :]]
print(first)
print(second)
print()

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic_countries = countries
print(first_country)
print(second_country)
print(third_country)
print(scandic_countries)