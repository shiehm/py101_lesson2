# Ask user for the first number
# Ask user for the second number
# Ask use for an operation
# Perform the operation
# Print results to the terminal

import json

# Open the JSON file for reading
with open('calc_msg.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f'-> {message}')

def invalid_num(num):
    try:
        float(num)
    except ValueError:
        return True
    return False

def invalid_op(operation):
    return operation not in data['op_dict']

while True:
    prompt(data["welcome"])
    
    prompt('Enter first number:')
    num1 = input()
    
    while invalid_num(num1):
        prompt(data["invalid_num"])
        num1 = input()
    
    prompt('Enter second number:')
    num2 = input()
    
    while invalid_num(num2):
        prompt(data["invalid_num"])
        num2 = input()
    
    prompt('Choose an operation:\n1. Add 2. Subtract 3. Multiply 4. Divide')
    operation = input()
    
    while invalid_op(operation):
        prompt('Error: Invalid operation')
        operation = input()
    
    if operation == '1':
        result = float(num1) + float(num2)
    elif operation == '2':
        result = float(num1) - float(num2)
    elif operation == '3':
        result = float(num1) * float(num2)
    elif operation == '4':
        result = float(num1) / float(num2)
    
    prompt(f'{num1} {data["op_dict"][operation]} {num2} = {result}')
    
    again = input('Do you want to run another calculation? (Y/N): ')
    if again.upper() != 'Y':
        break