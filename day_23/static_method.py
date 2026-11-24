class BankAccount:

    # class Variables

    bank_name = "Bank of Pakistan"
    interest_rate = 5.0


    # constructor

    def __init__(self, name, balance):
        self.owner = name
        self.balance = balance


    # Instance Methods

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully!!")
        print(f"Updated Balance: Rs. {self.balance}/-\n")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully!!")
        else:
            print("Insufficient funds!!")
        print(f"Updated Balance: Rs. {self.balance}/-\n")


    # Class Method
    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Interest rate changed to {cls.interest_rate}%\n")


    # static method
    @staticmethod
    def calculate_simple_interest(principal, year, time):
        interest = (principal * year * time) / 100
        return interest

# objects of BankAccount class

account1 = BankAccount("Ali", 10000)
account2 = BankAccount("Ahmed", 20000)

# Using instance methods

account1.deposit(1000)
account2.withdraw(5000)

# Using class method

BankAccount.change_interest_rate(6.0)

# Using static method

interest = BankAccount.calculate_simple_interest(10000,5, 7.0)
print(f"Simple Interest: Rs. {interest}/-")