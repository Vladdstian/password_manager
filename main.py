import account

adding_accounts = True
while adding_accounts:
    new_account = account.Account()
    print(new_account.account_details)
    adding_accounts = new_account.save_account()
