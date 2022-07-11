import random

while True:
    choice = ["rock", "paper", "scissors"]
    computer = random.choice(choice)
    player = None

    while player not in choice:
        player = input(" rock, paper, or scissors?: ").lower()
    if player == computer:
            print("computer: ", computer)
            print("player: ", player)
            print("tie")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you loose")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("win")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you loose")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("win")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you loose")

    play_again = input("play again: (yes/no): ").lower()

    if play_again  != "yes":
        break

print("Bye")
