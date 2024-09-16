"""
Rock Paper Scissor Spock Lizard Rules:
- Rock beats lizard, scissors
- Paper beats rock, spock
- Scissors beats paper, lizard
- Spock beats rock, scissors
- Lizard beats paper, spock
"""

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
SHORT_CHOICES = ['r', 'p', 'sc', 'sp', 'l']

WINNING_COMBOS = {
    'rock': ['lizard', 'scissors'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'spock': ['rock', 'scissors'],
    'lizard': ['paper', 'spock']
}

SHORT_CHOICES_MAP = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'sp': 'spock',
    'l': 'lizard'
}

def prompt(msg):
    print(f'-> {msg}')

def first_wins(user_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[user_choice]

def display_winner(user_choice, computer_choice):
    if first_wins(user_choice, computer_choice):
        prompt('You win this round!')
    elif first_wins(computer_choice, user_choice):
        prompt('You lose this round!')
    else:
        prompt('Tie!')

prompt('This is Rock, Paper, Scissors, Spock, Lizard. Best out of 5.')

computer_won = 0
user_won = 0

while (user_won < 3) or (computer_won < 3):
    prompt(f"Choose from: {', '.join(VALID_CHOICES)}")
    user_choice = input()

    while (user_choice not in VALID_CHOICES) and (user_choice not in SHORT_CHOICES):
        prompt(f"That was not a valid choice, choose from: {', '.join(VALID_CHOICES)}")
        user_choice = input()

    if user_choice in SHORT_CHOICES:
        user_choice = SHORT_CHOICES_MAP[user_choice]

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {user_choice}, the computer chose {computer_choice}')
    display_winner(user_choice, computer_choice)

    if first_wins(user_choice, computer_choice):
        user_won += 1
    elif first_wins(computer_choice, user_choice):
        computer_won += 1

    prompt(f'User Score: {user_won}/5')
    prompt(f'Computer Score: {computer_won}/5')

    if user_won == 3:
        prompt("You won the game!")
        break

    if computer_won == 3:
        prompt("You lost the game!")
        break

    prompt('Play again (y/n)?')
    again = input().lower()

    # while again[0] not in ['y', 'n']:
    while not (again.startswith('y') or again.startswith('n')):
        prompt('Invalid choice, please choose y/n')
        again = input().lower()

    if again[0] == 'n':
        break