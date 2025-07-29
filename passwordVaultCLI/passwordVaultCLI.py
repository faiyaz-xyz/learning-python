# 🔑 Project: Password Manager Lite – Phase 1

# 🔹 GOALS:

# 1. Save New Password
# 2. View Saved Passwords
# 3. Exit

# 🔹 Requirements:

# ✅ Save site name + username + password
# ✅ Store in a file (e.g. vault.txt)
# ✅ Show all saved entries nicely formatted
# ✅ Don't show passwords directly unless user confirms 👀
# ✅ File should be in the same folder as the script

import time
import os

folder_path = os.path.dirname(__file__)
password_file = os.path.join(folder_path, "vault.txt")


print("To use the following program follow the instructions:-")
time.sleep(1)
print("Type 'vault' before every instruction")
time.sleep(1)
print("Then type the number of instruction, e.g. vault 1")
time.sleep(1)
print("Here's the instructions available:-")
time.sleep(1)
print("1) Save New Password")
time.sleep(1)
print("2) View Saved Accounts")
time.sleep(1)
print("To exit terminal, type 'exit'")
time.sleep(1)
print("Happy typing passwords!")
time.sleep(1)

command = input("PasswordVault> ")

while command != "exit":
    if command == "vault 1":
        print("Enter the site name of the account you're using:-")
        siteName = input("PasswordVault> ")
        print("Enter the username of the account you're using:-")
        username = input("PasswordVault> ")
        print("Enter the password of the account you're using:-")
        password = input("PasswordVault> ")

        if siteName == "" or username == "" or password == "":
            print("\nPlease input all fields\n")
            continue

        with open(password_file, "a") as f:
            f.write(
                f"Site: {siteName} | User: {username} | Pass: {password}\n")

    elif command == "vault 2":
        print("Type the username and password of the account you want to access for verfication:-")
        username = input("PasswordVault> ")
        password = input("PasswordVault> ")

        showPassword = input("Show Password? (Y/N)")

        if showPassword.lower() == "y":
            line_found = False
            with open(password_file) as f:
                for line in f:
                    if f"User: {username}" in line and f"Pass: {password}" in line:
                        line_found = True
                        break

            if line_found:
                with open(password_file) as f:
                    print("\nSaved Accounts:")
                    for line in f:
                        print(line.strip())
            else:
                print("Username and password wasn't found!")
        else:
            print("Okay, not showing passwords. Back to main menu!")
    else:
        print("\nInvalid Command!\n")

    command = input("PasswordVault> ")
