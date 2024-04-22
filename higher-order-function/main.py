from functools import reduce

##################################


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



##################################



# Task 1 : Use map to create new list by change each country to upper case

def change_to_upper(countries) :
    return list(map(lambda country : str.upper(country), countries))

# Task 2 : Use map to create a new list by changing each number to its square in the numbers list

def change_to_square(numbers):
    return list(map(lambda x : x**2, numbers))


# Task 3: Use map to change each name to uppercase in the names list

def change_to_upper_name(names): 
    return list(map(lambda name : str.upper(name), names))

# Task 4: Use filter to filter out countries containing 'land'.

def filter_countries_contains(countries, keyword):
    return list(filter(lambda x : keyword not in x, countries))

# Task 5 : Use filter to filter out countries having exactly six characters.

def filter_countries_equal_six_characters(countries):
    return list(filter(lambda x : len(x) != 6, countries))

# Task 6: Use filter to filter out countries starting with an 'E'

def filter_countries_start_with_E(countries):
    return list(filter(lambda country :  country[0] != 'E', countries))

# Task 7 : Use reduce to sum all the numbers in the numbers list.

def sum_all(numbers): 
    return reduce(lambda x,y : x + y, numbers)


print(change_to_upper(countries))
print(change_to_square(numbers))
print(change_to_upper_name(names))
print(filter_countries_contains(countries, 'land'))
print(filter_countries_equal_six_characters(countries))
print(filter_countries_start_with_E(countries))
print(sum_all(numbers))

