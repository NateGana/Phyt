from Bank import Bank

# check if the amount was greater to zero since we can't withdraw or deposit amounting to zero
def get_amount(prompt):
    try:
        amount = float(input(prompt))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        return amount

    except ValueError as error: # exception error if accidentally typed string in float inputs
        if str(error) == "could not convert string to float: ":
            print("Error: Please enter a valid number.")
        else:
            print(f"Error: {error}")
        return None


def main():
    bank = Bank()

    while True:
        print("\n========== VILLANUEVA BANK ==========")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Display Account Information")
        print("6. Calculate Annual Interest")
        print("7. Display All Accounts")
        print("8. Exit")
        print("-------------------------------")
        choice = input("Enter your choice: ").strip() # strip to remove whitespaces
        print("-------------------------------")
        #create a new account
        try:
            if choice == "1":
                print("\nChoose Account Type")
                print("1. Savings Account")
                print("2. Checking Account\n")
                print("-----------------------------")
                account_choice = input("Enter choice: ").strip()

                if account_choice == "1": # creating savings account
                    account_type = "savings"
                elif account_choice == "2": # creating checking account
                    account_type = "checking"
                else:
                    print("Error: Invalid account type.")
                    continue

                account_number = input("Enter account number: ") #acc number
                name = input("Enter account holder name: ") #acc name

                initial_balance = input(
                    "Enter initial balance (default 0): "
                ).strip() #balance
                print("-------------------------------")
                balance = float(initial_balance) if initial_balance else 0.0 # put initial balance to balance

                account = bank.create_account(
                    account_type,
                    account_number,
                    name,
                    balance
                ) # creating the object for the account

                print("\nAccount created successfully!")
                account.display_info()  # show the newly created object
                print("-------------------------------")

            elif choice == "2": # method to check your balance
                account_number = input("Enter account number: ")
                account = bank.find_account(account_number)
                print("-------------------------------")
                print(f"Your Current Balance: PHP {account.balance:,.2f}")
                print("-------------------------------")
            elif choice == "3": # method to deposit
                print("-------------------------------")
                account_number = input("Enter account number: ")
                account = bank.find_account(account_number)

                amount = get_amount("Enter deposit amount: PHP ")

                if amount is not None:
                    account.deposit(amount)
                    print("-------------------------------")
                    print("Deposit successful!\n")
                    print(f"New Balance: PHP {account.balance:,.2f}")
                    print("-------------------------------")
            elif choice == "4": # method to withdraw 
                print("-------------------------------")
                account_number = input("Enter account number: ")
                account = bank.find_account(account_number)

                amount = get_amount("Enter withdrawal amount: PHP ")

                if amount is not None:
                    account.withdraw(amount)
                    print("-------------------------------")
                    print("Withdrawal successful!\n")
                    print(f"New Balance: PHP {account.balance:,.2f}")
                    print("-------------------------------")
            elif choice == "5": # method to see full details of your bank account
                print("-------------------------------")
                account_number = input("Enter account number: ")
                account = bank.find_account(account_number)
                account.display_info()
                print("-------------------------------\n")

            elif choice == "6": # method to calculate your annual interest
                print("-------------------------------")
                account_number = input("Enter account number: ")
                account = bank.find_account(account_number)

                interest = account.calculate_interest()
                print("-------------------------------")
                print(f"Account Type: {account.get_account_type()}")
                print(f"Annual Interest: PHP {interest:,.2f}")
                print("-------------------------------")
                if account.get_account_type() == "Savings Account":
                    apply = input(
                        "Apply this interest to the balance? (y/n): "
                    ).strip().lower()

                    if apply == "y":
                        interest = account.apply_annual_interest()
                        print("-------------------------------")
                        print(f"Interest added: PHP {interest:,.2f}")
                        print(f"New Balance: PHP {account.balance:,.2f}")
                        print("-------------------------------")

            elif choice == "7": # show basic information of all existing accounts
                print("-------------------------------")
                bank.show_basic_accounts()
                print("-------------------------------")
            elif choice == "8": # exit the program
                print("-------------------------------")
                print("Thank you for using the Python Banking System!")
                print("-------------------------------")
                break

            else:
                print("Error: Invalid menu choice. Please select 1-8.")

        except ValueError as error: # handle errors in typing
            print(f"Error: {error}")

        except (EOFError, KeyboardInterrupt):
            print("\nProgram terminated.")
            break

# prevent from running other class other than main
if __name__ == "__main__":
    main()