# 📅 Project: "Birthday Reminder App" (Console Version)

# 🎯 What it does:

# * You store your friends’ birthdays (name + date)
# * You can add new ones, view upcoming ones, or delete
# * You get a lil reminder if anyone’s birthday is today! 🎉

# ---

# 🧠 Concepts you’ll use:

# * Dictionaries
# * Date & time with `datetime`
# * Loops, conditionals, user input
# * File saving (optional)

import datetime
import time
import os

folder_path = os.path.dirname(__file__)
birthday_file = os.path.join(folder_path, "birthdays.txt")

print("Welcome to Birthday Reminder App!")
time.sleep(1)
print("Here's a guideline to save it correctly:-")
time.sleep(1)
print("Birthday date format should be in (DD/MM/YYYY) e.g. 02/08/2025")
print("If you get it wrong, it's your fault.")

friendBirthday = input(
    "Type your friend's birthday in the format, (DD/MM/YYYY) e.g. 02/08/2025 :- ")

with open(birthday_file, "a") as f:
    f.write(friendBirthday)
