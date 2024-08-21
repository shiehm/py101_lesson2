# You'll need three pieces of information:

# the loan amount
# the Annual Percentage Rate (APR)
# the loan duration in months

# monthly interest rate (APR / 12)

# m = p * (j / (1 - (1 + j) ** (-n)))

# m = monthly payment
# p = loan amount
# j = monthly interest rate
# n = loan duration in months

def prompt(message):
    print(f'-> {message}')

def invalid_float(num):
    try:
        num = float(num)
        if num <= 0:
            raise ValueError(f'Value must be > 0. You entered: {num}')
    except (TypeError, ValueError):
        return True
        
    return False

def monthly_mortgage(loan_amt, apr, months):
    month_apr = apr / 12
    monthly_due = loan_amt * (month_apr / (1 - (1 + month_apr) ** (-months)))
    return monthly_due

prompt('I am a mortgage calculator!')

prompt('What is the loan amount? ')
loan_amt = input('')
while invalid_float(loan_amt):
    prompt('Invalid amount entered.')
    loan_amt = input('')

prompt('What is the annual percentage rate (APR)? Enter as a decimal (e.g. 0.05 not 5%) ')
apr = input('')
while invalid_float(loan_amt):
    prompt('Invalid amount entered.')
    apr = input('')

prompt('What is the loan duration in months? ')
months = input('')
while invalid_float(loan_amt):
    prompt('Invalid amount entered.')
    months = input('')

loan_amt = float(loan_amt)
apr = float(apr)
months = float(months)

monthly_due = monthly_mortgage(loan_amt, apr, months)

prompt(f'Your {months:.0f} month {apr:.2%} ${loan_amt:.2f} loan requires a ${monthly_due:.2f} monthly payment.')