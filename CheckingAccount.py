from BankAccount import BankAccount


class CheckingAccount(BankAccount):
    def calculate_interest(self):
        return 0.0

    # return the type of account 
    def get_account_type(self):
        return "Checking Account"