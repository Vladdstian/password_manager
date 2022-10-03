import password_func
import os
import csv

# this block will execute once to create the csv file locally and add the column names
with open("Password.csv", "a", newline='') as file:
    writer = csv.writer(file)
    if os.path.getsize("Password.csv") == 0:
        column_names = ["website", "username", "password"]
        writer.writerow(column_names)
    else:
        pass


# this function is used to save the data inside the csv file
def save(account):
    with open("Password.csv", "a", newline='') as file:
        data_writer = csv.writer(file)
        data = [account["website"], account["username"], account["password"]]
        data_writer.writerow(data)


# Request user inputs for the new account
website = input("Please enter the website for which you are creating an account: ")
username = input("Please enter the username/email address you want to use for the account: ")
new_account = {"website": website, "username": username, "password": password_func.password_request()}

# Check if all the fields are filled and not empty -
# TODO - to be implemented inside the save function
for key in new_account:
    if new_account[key] == "":
        input_request = input(f"You haven't entered any {key}. Would you like to update it?")
        if input_request == 'y':
            new_account[key] = input(f"Please enter the {key} for which you are creating an account: ")
        else:
            new_account = {}
    else:
        continue

if new_account != {}:
    save(new_account)
else:
    pass
