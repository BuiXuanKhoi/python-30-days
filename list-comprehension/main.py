# Problem


##################################

#  Task 1: Filter only negative and zero using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

##################################


# Task 2: flatten to one dimension 
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

##################################

# Task 3: Flatten to list output

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


##################################

# Task 4: Change to list of dictionaries

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]


##################################

# Task 5 : Change list to list of concat strings: 

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

##################################

# Solution

def task1(numbers):
    return [i  for i in  numbers if i > 0]


def task2(input) :
    return [i for nested_list in input for sublist in nested_list for i in sublist]

def task3(input):
    return [[str.upper(sub_tuple[0]), str.upper(sub_tuple[0][0:3]), str.upper(sub_tuple[1])] for nested_list in input for sub_tuple in nested_list] 

def task4(input):
    return[{ 'country': str.upper(sub_tuple[0]), 'city' : str.upper(sub_tuple[1])} for nested_list in input for sub_tuple in nested_list]


def task5(input) :
    return [sub_tuple[0] + ' ' + sub_tuple[1] for nested_list in input for sub_tuple in nested_list]


print(task1(numbers))
print(task2(input= list_of_lists))
print(task3(input= countries))
print(task4(input= countries))
print(task5(input= names))
