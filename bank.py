from account import SavingsAccount, CurrentAccount


class Bank:

    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self, holder_name, account_type, initial_balance):
        account_number = f"ACC{self.next_account_number}"

        if account_type.lower() == "savings":
            account = SavingsAccount(
                account_number,
                holder_name,
                initial_balance
            )

        elif account_type.lower() == "current":
            account = CurrentAccount(
                account_number,
                holder_name,
                initial_balance
            )

        else:
            print("Invalid account type.")
            return None

        self.accounts[account_number] = account
        self.next_account_number += 1

        print("\nAccount created successfully!")
        print(f"Account Number: {account_number}")
        print(f"Account Holder: {holder_name}")
        print(f"Account Type: {account_type.title()}")

        return account

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def display_accounts(self):
        print("\n===== ALL BANK ACCOUNTS =====")

        if not self.accounts:
            print("No accounts available.")
            return

        for account in self.accounts.values():
            print(
                f"{account.account_number} | "
                f"{account.holder_name} | "
                f"Balance: ₹{account.balance:.2f}"
            )