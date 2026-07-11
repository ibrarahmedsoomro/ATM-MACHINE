class BankAccount:

    bank_name = "UBL"

    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.__balance += amount
            print(f"Deposit Successful! Current Balance: {self.__balance}")
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if not BankAccount.is_valid_amount(amount):
            print("Invalid Amount")

        elif amount > self.__balance:
            print("Insufficient Balance")

        else:
            self.__balance -= amount
            print(f"Withdrawal Successful! Current Balance: {self.__balance}")

    @classmethod
    def change_bank(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


# ------------------------
# Testing
# ------------------------

account = BankAccount("Ibrar Ahmed", 5000)

print("Bank:", BankAccount.bank_name)

account.deposit(2000)

account.withdraw(1000)

print("Current Balance:", account.get_balance())

BankAccount.change_bank("ABL")

print("New Bank Name:", BankAccount.bank_name)