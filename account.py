from abc import ABC, abstractmethod
from decimal import Decimal
from transaction import Transaction


class BankAccount(ABC):

    def __init__(self, account_number, holder_name, initial_balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = Decimal(str(initial_balance))
        self.__transactions = []

        if self.__balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        if self.__balance > 0:
            self.add_transaction("Initial Deposit", self.__balance)

    @property
    def account_number(self):
        return self.__account_number

    @property
    def holder_name(self):
        return self.__holder_name

    @property
    def balance(self):
        return self.__balance

    def _change_balance(self, amount):
        self.__balance += Decimal(str(amount))

    def add_transaction(self, transaction_type, amount):
        transaction = Transaction(
            transaction_type,
            amount,
            self.__balance
        )
        self.__transactions.append(transaction)

    def deposit(self, amount):
        amount = Decimal(str(amount))

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self._change_balance(amount)
        self.add_transaction("Deposit", amount)

        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        amount = Decimal(str(amount))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self._change_balance(-amount)
        self.add_transaction("Withdrawal", amount)

        print(f"₹{amount:.2f} withdrawn successfully.")

    def show_balance(self):
        print(f"Available Balance: ₹{self.__balance:.2f}")

    def show_transactions(self):
        print("\n===== TRANSACTION HISTORY =====")

        if not self.__transactions:
            print("No transactions found.")
            return

        for transaction in self.__transactions:
            transaction.display()

    @abstractmethod
    def apply_monthly_update(self):
        pass


class SavingsAccount(BankAccount):

    def __init__(self, account_number, holder_name, initial_balance):
        super().__init__(
            account_number,
            holder_name,
            initial_balance
        )

        self.interest_rate = Decimal("0.04")

    def apply_monthly_update(self):
        interest = (
            self.balance * self.interest_rate / Decimal("12")
        ).quantize(Decimal("0.01"))

        if interest > 0:
            self._change_balance(interest)
            self.add_transaction("Monthly Interest", interest)

        print(f"Monthly interest added: ₹{interest:.2f}")


class CurrentAccount(BankAccount):

    def __init__(self, account_number, holder_name, initial_balance):
        super().__init__(
            account_number,
            holder_name,
            initial_balance
        )

        self.maintenance_fee = Decimal("50.00")

    def apply_monthly_update(self):
        if self.balance >= self.maintenance_fee:
            self._change_balance(-self.maintenance_fee)

            self.add_transaction(
                "Maintenance Fee",
                self.maintenance_fee
            )

            print("Monthly maintenance fee of ₹50 charged.")

        else:
            print("Insufficient balance for maintenance fee.")