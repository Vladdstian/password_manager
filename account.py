import random
import os
import csv

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
ACCOUNTS = "Password.csv"


def generate_password(no_char):
    max_letters = int(no_char * 0.5)
    max_numbers = int(no_char * 0.25)
    max_symbols = int(no_char * 0.25)
    if max_symbols + max_numbers + max_letters != no_char:
        max_letters += no_char - (max_symbols + max_numbers + max_letters)
    password_letters = [random.choice(LETTERS) for _ in range(max_letters)]
    password_numbers = [random.choice(NUMBERS) for _ in range(max_numbers)]
    password_symbols = [random.choice(SYMBOLS) for _ in range(max_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    return password


# Added encrypt and decode functions to save account into the csv file details directly encrypted
def encrypt(message, shift):
    message_list = []
    coded_message = ""
    for letter in message:
        if letter in LETTERS:
            index = LETTERS.index(letter) + shift
            if index >= len(LETTERS):
                index -= len(LETTERS)
            message_list.append(LETTERS[index])
        else:
            message_list.append(letter)
    for letter in message_list:
        coded_message += letter
    return coded_message


def decode(message, shift):
    message_list = []
    decoded_message = ""
    for letter in message:
        if letter in LETTERS:
            index = LETTERS.index(letter) - shift
            if index < 0:
                index += len(LETTERS)
            message_list.append(LETTERS[index])
        else:
            message_list.append(letter)
    for letter in message_list:
        decoded_message += letter
    return decoded_message


class Account:
    def __init__(self):
        self.account_details = self.create_account()

    def create_account(self):
        website = input("Please enter the website for which you are creating an account: ")
        username = input("Please enter the username/email address you want to use for the account: ")
        password = self.password_request()
        account_details = {"website": website, "username": username, "password": password}
        return account_details

    def password_request(self):
        password_choice = int(input("Would you like to (1)add a password or (2)generate one? "))
        if password_choice == 1:
            password = input("Please type the password you desire: ")
            return password
        elif password_choice == 2:
            no_of_char = int(input("How many characters would you like your password to be? "))
            password = generate_password(no_of_char)
            return password
        elif password_choice == 3:
            print("Thank you for using password service!")
            password = ""
            return password
        else:
            print("I don't understand! Please try again or type (3) to cancel!\n\n")
            return self.password_request()

    def save_account(self, encrypt_decode_key):
        for key in self.account_details:
            if self.account_details[key] == "":
                input_request = input(f"You haven't entered any details for the {key}. Would you like to update it?("
                                      f"y/n) ")
                if input_request == 'y':
                    self.account_details[key] = input(f"Please enter the {key} for which you are creating an account: ")
                else:
                    self.account_details = {}
                    choice = input("Would you like to add another account? (y/n)")
                    if choice == 'y':
                        self.create_account()
                    else:
                        return False
        if self.account_details != {}:
            with open(ACCOUNTS, "a", newline='') as file:
                writer = csv.writer(file)
                if os.path.getsize(ACCOUNTS) == 0:
                    column_names = ["website", "username", "password"]
                    writer.writerow(column_names)
                website = encrypt(self.account_details["website"], encrypt_decode_key)
                username = encrypt(self.account_details["username"], encrypt_decode_key)
                password = encrypt(self.account_details["password"], encrypt_decode_key)
                writer.writerow([website, username, password])
                return True
