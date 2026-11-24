# ----------------> TYPE OF INHERITANCE <-----------------


# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# ------------> Single Inheritance <-----------

class Animal:

    def speak(self):
        print("Animal make a sound 🔊")

class Dog(Animal):

    def bark(self):
        print("Dog Bark woof!! 🐕")

# -----------> object

d = Dog()

d.speak()
d.bark()


# ------------> Multiple Inheritance <------------

class Father:

    def hobbies(self):
        print("Reading Newspaper 📰")

class Mother:

    def skills(self):
        print("Cooking tasty Biryani 🍛")

class Children(Father, Mother):

    def play(self):
        print("Playing Cricket 🏏")

# -----------> object

c = Children()

c.play()
c.hobbies()
c.skills()


# ----------> Multilevel Inheritance <-------------


class GrandFather:

    def house(self):
        print("Grandparent's House 🏡")

class Parent(GrandFather):

    def car(self):
        print("Parent's Car 🚗")

class Son(Parent):

    def bike(self):
        print("My Bike 🛵")

# ----------> object

f = Son()

f.bike()
f.car()
f.house()
    


# -----------> Hierarchical Inheritance <-----------

class Vehicle:

    def start(self):
        print("Vehicle Started 🚘")

class Car(Vehicle):

    def drive(self):
        print("Driving a Car 🚙")

class Bike(Vehicle):

    def ride(self):
        print("Riding a Bike 🏍")

# ----------> object

car = Car()
bike = Bike()

car.start()
bike.start()



# -----------> Hybrid Inheritance <------------

class A:

    def show_A(self):
        print("Showing Class 🅰")

class B(A):

    def show_B(self):
        print("Showing Class 🅱")

class C(A):

    def show_C(self):
        print("Showing Class C")

class D(B, C): # Hybrid Inheritance (Multilevel + Multiple)

    def show_D(self):
        print("Showing Class D")


# --------> object

d = D() 

d.show_A() # Inherited From A
d.show_B() # From B
d.show_C() # From C
d.show_D() # OWN