from bank import Bank
from decimal import Decimal, InvalidOperation


def get_amount(message):
    while True:
        try:
            amount = Decimal(input(message))

            if not amount.is_finite():
                print("Please enter a valid amount.")
                continue

            return amount

        except InvalidOperation:
            print("Invalid amount. Please enter numbers only.")


def main():
    bank = Bank()

    while True:
        print("\n========== PYTHON BANKING SYSTEM ==========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Display All Accounts")
        print("7. Apply Monthly Update")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter account holder name: ").strip()

            if not name:
                print("Name cannot be empty.")
                continue

            print("\n1. Savings Account")
            print("2. Current Account")

            account_choice = input("Select account type: ").strip()

            if account_choice == "1":
                account_type = "savings"
            elif account_choice == "2":
                account_type = "current"
            else:
                print("Invalid account type.")
                continue

            initial_balance = get_amount("Enter initial deposit: ₹")

            if initial_balance < 0:
                print("Initial deposit cannot be negative.")
                continue

            bank.create_account(name, account_type, initial_balance)

        elif choice in ["2", "3", "4", "5", "7"]:
            account_number = input("Enter account number: ").strip()
            account = bank.find_account(account_number)

            if account is None:
                print("Account not found.")
                continue

            if choice == "2":
                amount = get_amount("Enter deposit amount: ₹")
                account.deposit(amount)

            elif choice == "3":
                amount = get_amount("Enter withdrawal amount: ₹")
                account.withdraw(amount)

            elif choice == "4":
                account.show_balance()

            elif choice == "5":
                account.show_transactions()

            elif choice == "7":
                account.apply_monthly_update()

        elif choice == "6":
            bank.display_accounts()

        elif choice == "8":
            print("Thank you for using Python Banking System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()