from datetime import datetime


class Transaction:
    def __init__(self, transaction_type, amount, balance_after):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def display(self):
        print(
            f"{self.date} | {self.transaction_type} | "
            f"Amount: ₹{self.amount:.2f} | "
            f"Balance: ₹{self.balance_after:.2f}"
        )