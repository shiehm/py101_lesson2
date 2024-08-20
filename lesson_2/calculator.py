# Ask user for the first number
# Ask user for the second number
# Ask use for an operation
# Perform the operation
# Print results to the terminal

def prompt(message):
    print(f'-> {message}')

def invalid_num(num):
    try:
        int(num)
    except ValueError:
        return True
    return False

def invalid_op(operation):
    return operation not in op_dict

op_dict = {
    '1': '+',
    '2': '-',
    '3': '*',
    '4': '/'
}

prompt('Welcome to calculator.py!')

prompt('Enter first number:')
num1 = input()

while invalid_num(num1):
    prompt('Error: Number must be an integer.')
    num1 = input()

prompt('Enter second number:')
num2 = input()

while invalid_num(num2):
    prompt('Error: Number must be an integer.')
    num2 = input()

prompt('Choose an operation:\n1. Add 2. Subtract 3. Multiply 4. Divide')
operation = input()

while invalid_op(operation):
    prompt('Error: Invalid operation')
    operation = input()

if operation == '1':
    result = int(num1) + int(num2)
elif operation == '2':
    result = int(num1) - int(num2)
elif operation == '3':
    result = int(num1) * int(num2)
elif operation == '4':
    result = int(num1) / int(num2)

print(f'{num1} {op_dict[operation]} {num2} = {result}')