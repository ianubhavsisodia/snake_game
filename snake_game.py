print("WELCOME TO SNAKE-WATER-GUN GAME!!!\n")
import random
n = int(input('Enter number of rounds: '))
round = 1
user_win=0
CPU_win=0
while(round<=n):
    print("Round: ",round, "\n" )
    player = {"s":"snake", "w":"water", "g":"gun"}
    for key, value in player.items():
        print("Press", key, "for", value, "\n", end="")
    a = str(input("\nchoose your move:\n"))
    if a == "s":
        print("Your move is snake." )
    elif a == "w":
        print("Your move is water." )
    elif a == "g":
        print("Your move is gun." )
    else:
        print("\n\nChoose valid move!!\n\n", end="")
        
    CPU = ["snake", "water", "gun"]
    choice = random.choice(CPU)
    print("\nNow it's computer's turn.\n")
    print("Computer's move is",choice, "\n")
    
    if choice == "snake" and a == "w":
        CPU_win += 1
    elif choice == "snake" and a == "g":
        user_win += 1    
    elif choice == "water" and a == "s":
        user_win += 1
    elif choice == "water" and a == "g":
        CPU_win += 1
    elif choice == "gun" and a == "w":
        user_win += 1
    elif choice == "gun" and a == "s":
        CPU_win += 1
    else:
        print("\nSame move, it's a draw.")

    if user_win>CPU_win:
        print("Player won round",round,"\n")
    elif CPU_win>user_win:
        print("Computer won round",round,"\n")    
    else:
        print("Draw!!!\n")
    round_left = print(n-round,"rounds left\n")
    round=round+1
    score = print("Your Score is",user_win,"\n")

if user_win>CPU_win:
    print("Congratulations!!! You Won\n","You won the game in",round,"rounds.")
elif CPU_win>user_win:
    print("You Lose!!!")
else:
    print("Game Draw!!")

    


    