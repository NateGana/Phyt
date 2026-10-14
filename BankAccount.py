from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, name, balance=0.0): # initialized the constructor

        if not account_number or not str(account_number).strip(): # account number cannot be empty
            raise ValueError("Account number cannot be empty.")

        if not name or not name.strip(): # account name cannot be empty
            raise ValueError("Account name cannot be empty.")

        if balance < 0: # initial balance can't be negative
            raise ValueError("Initial balance cannot be negative.")

        self.__account_number = str(account_number)
        self.__name = name.strip()
        self.__balance = float(balance)

    # Encapsulation: protected data is accessed through properties
    @property
    def account_number(self):
        return self.__account_number

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    # actual method for depositing
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.__balance += amount
        return self.__balance
    # actual method for withdrawing
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance.")

        self.__balance -= amount
        return self.__balance
    
    # to calculate interest
    @abstractmethod
    def calculate_interest(self):
        pass
    # to get account type
    @abstractmethod
    def get_account_type(self):
        pass
    
    # display full account information
    def display_info(self):
        print("\n----- ACCOUNT INFORMATION -----")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type:   {self.get_account_type()}")
        print(f"Balance:        PHP {self.balance:,.2f}")

    # display the basic account information
    def display_acc(self):
        print("\n----- BASIC ACCOUNT INFO -----")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type:   {self.get_account_type()}")
