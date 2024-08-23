import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(msg):
    print(f'-> {msg}')
    
def display_winner(user_choice, computer_choice):
    if ((user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissor' and computer_choice == 'paper')):
        prompt('You Win!')
    elif user_choice == computer_choice:
        prompt('Tie!')
    else:
        prompt('You Lose!')

while True:
    prompt(f"Choose from: {', '.join(VALID_CHOICES)}")
    user_choice = input() 
    
    while user_choice not in VALID_CHOICES:
        prompt(f"That was not a valid choice, choose from: {', '.join(VALID_CHOICES)}")
        user_choice = input() 
    
    computer_choice = random.choice(VALID_CHOICES)
    
    prompt(f'You chose {user_choice}, the computer chose {computer_choice}')
    display_winner(user_choice, computer_choice)
    
    prompt('Play again (y/n)?')
    again = input().lower()
    
    # while again[0] not in ['y', 'n']:
    while not (again.startswith('y') or again.startswith('n')):
        prompt('Invalid choice, please choose y/n')
        again = input().lower()
        
    if again[0] == 'n':
        break