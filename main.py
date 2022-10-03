import password_func
import os
import csv

with open("Password.csv", "a", newline='') as file:
    writer = csv.writer(file)
    if os.path.getsize("Password.csv") == 0:
        column_names = ["website", "username", "password"]
        writer.writerow(column_names)
    else:
        pass


def save(account):
    # TODO - update the function so that it will write only the first time the line with the column names
    with open("Password.csv", "a", newline='') as file:
        data_writer = csv.writer(file)
        data = [account["website"], account["username"], account["password"]]
        data_writer.writerow(data)


website = input("Please enter the website for which you are creating an account: ")
username = input("Please enter the username/email address you want to use for the account: ")
new_account = {"website": website, "username": username, "password": password_func.password_request()}

for key in new_account:
    if new_account[key] == "":
        print(f"You haven't entered any {key}. Would you like to update it?")
        new_account = {}
    else:
        continue

if new_account != {}:
    save(new_account)
else:
    pass
