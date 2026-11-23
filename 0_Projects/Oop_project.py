class Student:

    def __init__(self,name,roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}"


    def __lt__(self, other):
        return self.marks < other.marks


    def __eq__(self, value):
        return self.marks == value.marks


students = []

def add_student():

    name = input("Enter student name: ")

    roll_no = input("Enter student roll number: ")

    try:
        marks = float(input("Enter student marks: "))
    except ValueError:
        print("Invalid input for marks. Please enter a numeric value.")
        return

    student = Student(name = name, roll_no = roll_no, marks = marks)
    students.append(student)


    print(f"Student added successfully!")


def display_students():
    if not students:
        print("No students in the system logged yet.\n")
        return

    for s in students:
        print(s)
    print()



def compare_students():
    if len(students) < 2:
        print("need at least 2 students to compare.\n")
        return

    print("Comparing first two students in list:")
    s1,s2 = students[0], students[1]

    print(f"Student 1: {s1}")
    print(f"Student 2: {s2}")

    if s1 > s2:
        print(f"{s1.name} has more marks than {s2.name}.")
    elif s1 < s2:
        print(f"{s2.name} has more marks than {s1.name}.")
    else:
        print(f"{s1.name} and {s2.name} have equal marks.")



def menu():
    while True:

        print("\n---------------Student Management System---------------")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Compare Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()

        elif choice == '2':
            display_students()

        elif choice == '3':
            compare_students()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    menu()