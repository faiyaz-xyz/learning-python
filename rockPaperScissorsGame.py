# 🧠 CHALLENGE: **“Rock, Paper, Scissors” Game!**

# 🎯 GOAL:

# * You vs Computer
# * Track scores
# * Add animations like `“Rock…”` → wait 1s → `“Paper…”` → wait 1s → `“Shoot!”`

import random

rounds = int(
    input("How many rounds of Rock, Paper and Scissors do you want to play? :- ")
)

computerWinRate = 0
userWinRate = 0
drawRate = 0

for i in range(rounds):
    playerTurn = input("Choose your move (rock, paper, scissor):- ")
    computerTurn = int(random.randint(1, 3))
    if playerTurn.lower() == "rock":
        if computerTurn == 1:
            print("✊")
            print("It's a draw!")
            drawRate += 1
        elif computerTurn == 2:
            print("🖐")
            print("You lost this round!")
            computerWinRate += 1
        elif computerTurn == 3:
            print("✌")
            print("You won this round!")
            userWinRate += 1
    elif playerTurn.lower() == "paper":
        if computerTurn == 1:
            print("✊")
            print("You won this round!")
            userWinRate += 1
        elif computerTurn == 2:
            print("🖐")
            print("It's a draw!")
            drawRate += 1
        elif computerTurn == 3:
            print("✌")
            print("You lost this round!")
            computerWinRate += 1
    elif playerTurn.lower() == "scissor":
        if computerTurn == 1:
            print("✊")
            print("You lost this round!")
            computerWinRate += 1
        elif computerTurn == 2:
            print("🖐")
            print("You won this round!")
            userWinRate += 1
        elif computerTurn == 3:
            print("✌")
            print("It's a draw!")
            drawRate += 1
    else:
        print("Type a valid move!")

print("SCORE ANNOUNCEMENT!")
print(f"You won {userWinRate} times!\nAnd lost {computerWinRate} times...\nAnd had a draw {drawRate} times")
