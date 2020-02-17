from random import randint 

lst = ["rock", "paper", "scissors"]

computer = lst[randint(0,2)]

player = False

while player == False:
        player = input("play!")
        if player == computer:
           print("tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
             print("enter a valid option")
             player = False
             computer = lst[randint(0,2)]
