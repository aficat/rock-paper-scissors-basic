# This program is a rock-paper-scissors game is programmed to play the game with a computer.
# The computer would be given a random generated object for the game, (either rock, paper or scissors).

import random # to import random function into this file

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")

rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print("Computer picked: " + computer)

# paper beats rock
# rock beats scissors
# scissors beats paper

if player1 == computer:
    print("It's a tie!")
elif player1 == "rock":
    if computer == "scissors":
        print("Player 1 wins!")
    else:
        print("Computer wins!")
elif player1 == "paper":
    if computer == "rock":
        print("Player 1 wins!")
    else:
        print("Computer wins!")
elif player1 == "scissors":
    if computer == "paper":
        print("Player 1 wins!")
    else:
        print("Computer wins!")
else:
    print("Something went wrong!")
