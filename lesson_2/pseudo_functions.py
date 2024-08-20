# a function that returns the sum of two numbers
# 1. GET the first number from the user and SET a variable to = it
# 2. GET the second number from the user and SET a variable to = it
# 3. SET a result variable = first number + second number 
# 4. RETURN and PRINT the result variable 
# 5. END

def add(num1, num2):
    num1 = int(input('first number: '))
    num2 = int(input('second number: '))
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
    return result


    
# a function that takes a list of strings, 
# and returns a string that is all those strings concatenated together
# 1. GET a list of strings from the user:
# 1a. Create an empty list
# 1b. GET each value one by one from the user using a loop
# 1c. Stop the program upon a command from the user 
# 2. GET the seperator, if any from the user (i.e. comma, space, space and comma, etc.)
# 3. PRINT the list concatenated with the seperator, RETURN the combined string. END.

def string_concatenator():
    
    print('To exit the loop and return the list, type "STOP()"')
    
    str_list = []
    while True:
        value = input('Enter a string: ')
        if value == 'STOP()':
            break
        str_list.append(value)
    
    sep = input('Choose a separator: ')
    full_string = sep.join(str_list)
    print(full_string)
    
    return full_string


    
# a function that takes a list of integers, 
# and returns a new list with every other element from the original list, 
# starting with the first element. 

# If we want to just pass a list to the function:
# 1. Filter the list for only odd index (every other index position)
# 2. Return the list

# If we want to create the list via user input:
# 1. Create a list of integers:
# 1a. Create an empty list
# 1b. GET each value one by one from user input
# 1c. Turn each value into an integer, and save it to the list
# 1d. If the input is not a number, throw an error message but continue running
# 1e. Stop the program upon some command from the user
# 2. Pass this to the first function (modular method better than stacking it)

def create_int_list():
    int_list = []
    print('Type "STOP()" to finish the list')
    while True:
        value = input('Enter an integer: ')
        if value == 'STOP()':
            break
        int_list.append(int(value))
    return int_list

def every_other_int(int_list):
    new_list = []
    for i in range(len(int_list)):
        if i % 2 == 0:
            new_list.append(int_list[i])
    return new_list

# Pass a function to a function! 
# print(every_other_int(create_int_list()))



# a function that determines the index of the 3rd occurrence of a given character in a string. 
# For instance, if the given character is 'x' and the string is 'axbxcdxex', 
# the function should return 6 (the index of the 3rd 'x'). 
# If the given character does not occur at least 3 times, return None.

# 1. SET 2 variables = 0, one for the cumulative index, one for the number of occurances
# 2. Find the first occurance of the character in the string, add += index, occurances += 1
# 3. Repeat step 2 until occurances = 3
# 4. If fail to find another occurance, return None
# 5. Return the integer representing the index of the 3rd character

def third_occur(string, char):
    occurances = 0
    position = 0
    while occurances < 3:
        sub_index = string[position:].find(char)
        if sub_index == -1:
            print('This character is not found')
            return None
        
        occurances += 1
        position += (sub_index + 1)
        
        print(f'Found {occurances} occurance of {char} at index {position - 1}')
    
    index = position - 1
    
    print(f'The 3rd occurance of {char} in {string} found at index {index}.')
    print(f'checking {string[index]} = {char}')
    
    return index
    
# Use this to test: 
# third_occur('mississippi', 's')



# a function that takes two lists of numbers and 
# returns the result of merging the lists. 
# The elements of the first list should become 
# the elements at the even indexes of the returned list, 
# while the elements of the second list should become the 
# elements at the odd indexes. 

# 1. Calculate the total number of elements in both lists
# 2. Create an empty merged list
# 3. Insert elements of list1 in the even indices going up
# 4. Insert elements of list2 in the odd indices going up
# 5. Create a check to ensure the lists are of equal length (optional)

def merge(list1, list2):
    new_list = []
    length = len(list1) + len(list2)
    
    for i in range(0, length, 2):
        n = 0 if i == 0 else int(i / 2)
        new_list.insert(i, list1[n])
    
    for i in range(1, length, 2):
        n = int(((i + 1) / 2) - 1)
        new_list.insert(i, list2[n])
    
    print(new_list)
    return new_list
    
# Testing here:
# list1 = [1, 3, 5, 7]
# list2= [2, 4, 6, 8]
# merge(list1, list2)
