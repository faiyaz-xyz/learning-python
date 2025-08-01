import random
import time

responses = [
    "Yes, absolutely!",
    "No way!",
    "Maybe... try again?",
    "Ask again later 🤔",
    "I don't think so 👀",
    "Definitely!",
    "Nah fam 😂",
    "Signs point to yes",
    "Outlook not so good",
    "Trust your gut 😌"
]

print("Welcome to the Magic 8 Ball's area!")
time.sleep(1)

print("Ask your questions and type 'quit' to exit")
time.sleep(1)

questions = input("Ask the Magic 8 Ball your questions :- ")
time.sleep(1)

while questions != "quit":
    print("THE MAGIC BALL HAS ANSWERED YOUR FATE!")
    time.sleep(1)

    print(random.choice(responses))

    questions = input("Ask the Magic 8 Ball your questions :- ")
