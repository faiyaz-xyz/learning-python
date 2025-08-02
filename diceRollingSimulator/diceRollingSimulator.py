# 🎲 Project: Dice Rolling Simulator
# Every time user hits enter, it rolls a dice (1–6) and shows the result. Super simple, satisfying, and random 😎

# Goals:

# 🎲 Option to roll multiple dice :- IDK HOW TO

# 🎨 ASCII art for each dice face :- DONE

# 🔁 Loop until user types “stop” :- DONE

import random
import time

print("Welcome to the Dice Rolling Simulator!")
time.sleep(1)
print("Press ENTER to roll a dice")
print("Type 'stop' to quit")
time.sleep(1)

turn = input("Start? :- ")

while turn.lower() != 'stop':
    dice = random.randint(1, 6)

    if dice == 1:
        print("\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬛️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️\n")
    elif dice == 2:
        print("\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬛️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬛️⬜️\n⬜️⬜️⬜️⬜️⬜️\n")
    elif dice == 3:
        print("\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬛️⬜️⬜️⬜️\n⬜️⬜️⬜️⬛️⬜️\n⬜️⬛️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️\n")
    elif dice == 4:
        print("\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬛️⬜️⬛️⬜️\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬛️⬜️⬛️⬜️\n⬜️⬜️⬜️⬜️⬜️\n")
    elif dice == 5:
        print("\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬛️⬜️⬛️⬜️\n⬜️⬜️⬛️⬜️⬜️\n⬜️⬛️⬜️⬛️⬜️\n⬜️⬜️⬜️⬜️⬜️\n")
    elif dice == 6:
        print("\n⬜️⬜️⬜️⬜️⬜️\n⬜️⬛️⬛️⬛️⬜️\n⬜️⬛️⬛️⬛️⬜️\n⬜️⬛️⬛️⬛️⬜️\n⬜️⬜️⬜️⬜️⬜️\n")

    turn = input("Roll Again? :- ")
