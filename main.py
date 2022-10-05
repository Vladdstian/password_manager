import account

adding_accounts = True
while adding_accounts:
    new_account = account.Account()
    print(new_account.account_details)
    encrypt_code = input("Please enter a key for encryption: ")
    adding_accounts = new_account.save_account(encrypt_code)
    # TODO - Figure a way to remember the encryption code for each account
