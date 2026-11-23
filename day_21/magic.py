# OOP Magic/Dunder Methods


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Use the __str__ magic method to define how the object should be represented as a string

    def __str__(self):
        return f"{self.title} by {self.author}"


book = Book('Python Rocks!', 'Jose Portilla')
book1 = Book("Key to Happiness", "Robert")

print(book)  # Output: Python Rocks! by Jose Portilla
print(book1)  # Output: Key to Happiness by Robert


# ---------------------------------------------------------

class Money:

    def __init__(self, amount):
        self.amount = amount

# Use the __add__ magic method to define how two Money objects should be added together

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"${self.amount}"

wallet1 = Money(100)
wallet2 = Money(50)

total = wallet1 + wallet2
print(total)  # Output: $150


# ---------------------------------------------------

class Team:

    def __init__(self,members):
        self.members = members

# use the __len__ magic method to define how the length of the Team object should be calculated
    def __len__(self):
        return len(self.members)

# use the __repr__ magic method to define how the Team object should be represented as a string
    def __repr__(self):
        return f"Team({self.members})"

my_list = ['Ali','Faizan','Usman','Kino','Coyotito']
t1 = Team(['Juana','John','Steinbeck','Faizan'])


print((my_list))
print((t1))

print(len(my_list))
print(len(t1))
