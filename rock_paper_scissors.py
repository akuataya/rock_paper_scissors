# OK create rules
# OK ask user input
# OK generate random computer move
# OK print computer move
# OK compare computer move to user input
# OK print winner

import random

possible_moves = ["rock", "paper", "scissors"]

# maybe todo: I could add a while loop or something to validate input (remember set_pin?)
player_move = input("What's your move: rock, paper, or scissors? ")

computer_move = random.choice(possible_moves)
print("Computer's move: " + computer_move)

if player_move == computer_move:
    print("It's a tie!")
elif player_move == 'rock' and computer_move == 'scissors':
    print("You win! Rock beats scissors.")
elif player_move == 'paper' and computer_move == 'rock':
    print("You win! Paper beats rock.")
elif player_move == 'scissors' and computer_move == 'paper':
    print("You win! Scissors beat paper.")
else:
    print("You lose! " + computer_move.capitalize() + " beats " + player_move + ".")