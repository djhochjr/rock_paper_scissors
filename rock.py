import random
import time
import sys

print("****************************************")
print("Welcome to Rock-Paper-Scissors !")
print("****************************************")

#Create the data structure
options = {1: 'Paper', 2: 'Rock', 3:'Scissors'}

#Store the player's choice
def players_choice():
    #Get the players choice
    while True:
        pchoice = input("Enter your choice:\n 1 - Paper\n 2 - Rock\n 3 - Scissors\n or Q to exit\n")
        if pchoice == 'Q' or pchoice == 'q':
            sys.exit("Goodbye!")
        elif (pchoice == '1' or pchoice == '2' or pchoice == '3'):
            break
        else:
            print("Not a valid choice, try again!")
    print("You chose", options[int(pchoice)])
    pchoice = int(pchoice)
    return pchoice

def computers_choice():
    #Computer chooses
    comp_choice = random.randrange(1, 4)
    #Displays the computer's choice
    print("Computer chose", options[comp_choice])
    return comp_choice

def compare(pchoice, comp_choice):
    result = (pchoice, comp_choice)
    #comparisons
    if result == (1, 1) or result == (2, 2) or result == (3, 3):
        print("It's a tie!")
    elif result == (1, 2) or result == (2, 3) or result == (3, 1):
        print("You win")
    elif result == (1, 3) or result == (2, 1) or result == (3, 2):
        print("You lose!")
    else:
        print("Something went wrong")

def turns():
    for counter in range(1, 4):
        print("This is round", counter)
        pchoice = players_choice()
        comp_choice = computers_choice()
        compare(pchoice, comp_choice)
    exit()

if __name__ == '__main__':
    turns()