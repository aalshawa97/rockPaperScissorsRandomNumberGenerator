import random


def check_win(player, computer):
    print('Player choose: ' + player)
    print('Computer choose: ' + computer)

    if player == computer:
        print("Tie!")
    elif player == 'rock' and computer == 'paper':
        print('Computer wins')
    elif player == 'rock' and computer == 'scissors':
        print('Player wins')
    elif player == 'scissors' and computer == 'paper':
        print('Player wins')
    elif player == 'scissors' and computer == 'rock':
        print('Computer wins')
    elif player == 'paper' and computer == 'rock':
        print('Player wins')
    elif player == 'paper' and computer == 'scissors':
        print('Computer wins')


if __name__ == '__main__':
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)  # Fix: Remove the list brackets
    check_win(player_choice, computer_choice)
