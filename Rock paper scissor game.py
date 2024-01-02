from getpass import getpass as input
print("Rock paper Scissor Game")
print("For Rock type 'r'")
print("For Paper type 'p'")
print("For Scissor type 's'")

player1 = input("Player 1: What do you choose? Rock/paper/scissor ")
player2 = input("Player 2: What do you choose? Rock/paper/scissor ")

if player1 == "r" and player2 == "p":
    print("Paper covers rock. Player 2 wins.")
elif player1 == "r" and player2 == "s":
    print("Rock breaks scissor. Player 1 wins.")
elif player1 == "p" and player2 == "r":
    print("Paper covers rock. Player 1 wins.")
elif player1 == "p" and player2 == "s":
    print("Scissor cuts paper. Player 2 wins.")
elif player1 == "s" and player2 == "r":
    print("Rock breaks scissor. Player 2 wins.")
elif player1 == "s" and player2 == "p":
    print("Scissor cuts paper. Player 1 wins.")
elif player1 == player2:
    print("It's a tie.")

print("Input of player 1:", player1)
print("Input of player 2:", player2)