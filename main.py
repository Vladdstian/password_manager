import random


def generate_password(no_of_char):
    return no_of_char


new_account = {}
website = input("Please enter the website for which you are creating an account: ")
new_account["website"] = website

username = input("Please enter the username/email address you want to use for the account: ")
new_account["username"] = username

password_setup = True
while password_setup:
    password_choice = int(input("Would you like to (1)add a password or (2)generate one? "))
    if password_choice == 1:
        password = input("Please type the password you desire: ")
        new_account["password"] = password
        password_setup = False
    elif password_choice == 2:
        no_of_char = int(input("How many characters would you like your password to be? "))
        password = generate_password(no_of_char)
        new_account["password"] = password
        password_setup = False
    elif password_choice == 3:
        print("Thank you for using password service!")
        new_account["password"] = ""
        break
    else:
        print("I don't understand! Please try again or type (3) to cancel!\n\n")
        continue

for key in new_account:
    if new_account[key] == "":
        new_account = {}
    else:
        continue

print(new_account)
