# This program is a rock-paper-scissors game that helps to practice multiple "if" statements.

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
print("*** NO CHEATING ***! \n\n" * 20)
player2 = input("Player 2, make your move: ")

# paper beats rock
# rock beats scissors
# scissors beats paper

if player1 == "rock" and player2 == "scissors":
    print("Player 1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Something went wrong!")