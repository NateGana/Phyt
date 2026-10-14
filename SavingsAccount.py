from BankAccount import BankAccount

# abstract class for savings account that is inherited to BankAccount class
class SavingsAccount(BankAccount):
    
    interestRate = 0.04 #fixed rate for annual interest

    def calculate_interest(self):

        #to get the interest is to multiply balance to annual rate
        interest = self.balance * self.interestRate 
        return interest

    #method to apply the annual interest of the savings account
    def apply_annual_interest(self): 
        interest = self.calculate_interest()
        self.deposit(interest)
        return interest # return the interest 

    # return the account types
    def get_account_type(self):
        return "Savings Account"