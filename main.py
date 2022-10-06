import account
import file_management

local_key = file_management.generate_local_key()
file_management.create_file()
print(local_key)

adding_accounts = True
while adding_accounts:
    choice = input("Would you like to add an account?")
    if choice == "y":
        new_account = account.Account()
        print(new_account.account_details)
        adding_accounts = new_account.save_account()
    else:
        adding_accounts = False

code = int(input("Press 1 to encode and 2 to decode: "))
if code == 1:
    file_management.encrypt_file(local_key)
else:
    file_management.decrypt_file(local_key)
