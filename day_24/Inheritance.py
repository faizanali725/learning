# Inheritance 

# Parent class

class Animal:

    def __init__(self, name):
        self.name = name


    def sound(self):
        print(f"{self.name} makes a sound.\n")

    def eating(self):
        print(f"{self.name} is eating.\n")

# Child class

class Dog(Animal):

    def sound(self):
        print(f"{self.name} barks!!\n")

    def  dog_sniffs(self):
        print(f"{self.name} is sniffing around.\n")

    def color(self):
        print(f"{self.name} is a dog with a unique color.\n")

# Child class

class Cat(Animal):
    
    def sound(self):
        print(f"{self.name} meows!!\n")

    def cat_scratches(self):
        print(f"{self.name} is scratching the furniture.\n")

    def color(self):
        print(f"{self.name} is a cat with a white color.\n")

# objects

buddy = Dog("Buddy")
catto = Cat('Catto')
animal = Animal("Mike")

# Use instance method

buddy.sound()  # Inherited method from Animal class
buddy.dog_sniffs()  # Method specific to Dog class
buddy.eating()  # Inherited method from Animal class
buddy.color()  # Method specific to Dog class

print('-----------------------------')

catto.sound()
catto.color()
catto.cat_scratches()
catto.eating()

print("----------------------------")

animal.sound()



# Method Overloading

class Calculator:

    def add(self, a, b=0, c=0):
        return a+b+c

calc = Calculator()

result = calc.add(10)
print(result)


# Method Overriding and Super()

class Vehicle:

    def __init__(self):
        self.brand = "Honda"
        self.year = 2025

    def start_engine(self):
        return "Engine Started..."

    def description(self):
        return f"{self.year}: {self.brand} - vehicle"


class Car(Vehicle):

    def __init__(self, model, color):

        super().__init__()  # call parent constructor..

        self.model = model
        self.color = color

        print(f"Instance of car class created with Brand: {self.brand} & Year: {self.year}.\n")

    def description(self):
        return f"Model: {self.model} | color: {self.color}"

    def start_engine(self):
        return "Car Engine started with push button!!"




print("\n --------> Parent object <-------\n")

v1 = Vehicle()
print(v1.description())
print(v1.start_engine())


print("\n --------> Child object <-------\n")

c1 = Car("BMW","Black")
print(c1.description())
print(c1.start_engine())