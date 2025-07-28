valid_ops = ["+", "-", "*", "/"]

command = input(
    "Choose your operation (+, -, *, /) or type 'exit' to quit :- ")

while command != "exit":
    if command not in valid_ops:
        print("Invalid operation!")
        command = input(
            "Choose your operation (+, -, *, /) or type 'exit' to quit :- ")
        continue

    amountOfNumbers = int(input("How many numbers will you like to use? :- "))

    numbersUsing = []

    for i in range(amountOfNumbers):
        number = int(input("Input your number :- "))
        numbersUsing.append(number)

    if command == "+":
        total = sum(numbersUsing)
        print(f"Your sum is :- {total}")
    elif command == "-":
        difference = numbersUsing[0]
        for numbers in numbersUsing[1:]:
            difference -= numbers
        print(f"Your difference is :- {difference}")
    elif command == "*":
        product = 1
        for numbers in numbersUsing:
            product *= numbers
        print(f"Your product is :- {product}")
    elif command == "/":
        quotient = numbersUsing[0]
        is_invalid = False
        for numbers in numbersUsing[1:]:
            if numbers == 0:
                print("Cannot divide by zero!")
                is_invalid = True
                break
            quotient /= numbers

        if not is_invalid:
            print(f"Your quotient is: {quotient}")

    command = input(
        "Choose your operation (+, -, *, /) or type 'exit' to quit :- ")
