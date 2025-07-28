'''

### 🔹 Phase 1: Add & Show Tasks Only

* Show a menu:
  `1. Add Task`
  `2. View Tasks`
  `3. Exit`

* When user adds a task, save it to a text file (`todo.txt`)

* When viewing, read from the file and print each task

'''

import os

folder_path = os.path.dirname(__file__)
todo_file = os.path.join(folder_path, "todo.txt")

print("1. Add Task\n2. View Tasks\n3. Exit")
currentCommand = input(
    "Type the index of your command (e.g. 1 for adding a task) :- ")

while currentCommand != "3":
    if currentCommand == "1":
        task = input("Type in your task :- ")
        with open(todo_file, "a") as todo:
            todo.write(task + "\n")
    elif currentCommand == "2":
        with open(todo_file) as todo:
            task = todo.read().strip()
            if task:
                print("Tasks:")
                print(task)
            else:
                print("No tasks yet! 🚫")
    else:
        print("Invalid input!")

    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    currentCommand = input(
        "Type the index of your command (e.g. 1 for adding a task) :- ")
