# Encapsulation in Python is a concept that restricts access to certain attributes and methods of an object.
# It is a way to protect the internal state of an object from unintended interference and misuse.
# In Python, encapsulation is achieved using private attributes and methods,
# which are denoted by a double underscore prefix (e.g., __attribute).

class BankAccount:

    def __init__(self,owner, balance):
        self.owner = owner
        self.__balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs. {amount}/- to the account.")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew Rs. {amount}/- from the account.")
        else:
            print("Insufficient funds.")


    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account Owner: {self.owner}, Balance Rs.{self.__balance}/-"


account = BankAccount(owner = "John Doe", balance = 10000)

print(account)

account.deposit(5000)
account.withdraw(2000)
print(account)
