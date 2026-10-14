from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount


class Bank: 
    def __init__(self):
        self.__accounts = {}

    def create_account(self, account_type, account_number, name, balance=0.0):
        account_number = str(account_number).strip()

        if account_number in self.__accounts:
            raise ValueError("Account number already exists.")

        account_type = account_type.lower().strip()

        # save the object to respective account type

        if account_type == "savings": 
            account = SavingsAccount(account_number, name, balance)
        elif account_type == "checking":
            account = CheckingAccount(account_number, name, balance)
        else:
            raise ValueError("Account type must be savings or checking.")

        self.__accounts[account_number] = account
        return account

    def find_account(self, account_number): # method for finding existing accounts only, return not found if not found
        account_number = str(account_number).strip() 

        if account_number not in self.__accounts: # if acc number does not match to the existing array of accounts, return acc not found
            raise ValueError("Account not found.")

        return self.__accounts[account_number] # if found return the account number

    def show_all_accounts(self):
        if not self.__accounts:
            print("\nNo accounts have been created.")
            return

        for account in self.__accounts.values(): # loop through accounts to display
            account.display_info()

   
    def show_basic_accounts(self):
        if not self.__accounts:
            print("\nNo accounts have been created.")
            return

        for account in self.__accounts.values(): # loop through accounts to display
            account.display_acc()