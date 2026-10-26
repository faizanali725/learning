
# ---------------------> STUDENT CLASS <------------------------------

class Student:

    def __init__(self,student_id:int,name:str,father_name:str,age:int,gender:str,class_name:str,email:str,phone_number:str,address:str,marks:int):
        self.student_id = student_id
        self.name = name
        self.father_name = father_name
        self.age = age
        self.gender = gender
        self.class_name = class_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.marks = marks
        self.subject_marks_dict = {}



    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Student Father's Name: {self.father_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Class: {self.class_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")
        print(f"Marks: {self.marks}")
        for subject, marks in self.subject_marks_dict.items():
            print(f"{subject}: {marks}")



    def calculate_grade(self):

        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        elif self.marks >= 50:
            return 'E'
        else:
            return 'F'



    def add_marks(self):

        num_subjects = int(input("Enter the number of subjects: "))
        count = 0

        while count < num_subjects:
            subject = input("Enter Subject Name: ")

            if subject in self.subject_marks_dict:
                print(f"{subject} already exists. Please enter a different subject.")
                continue

            marks = int(input("Enter Subject Marks: "))
            self.subject_marks_dict[subject] = marks

            count += 1

        print("All subjects added successfully!")

        print()
        print('------------------------------------------------------')




    def calculate_average(self):
        total_marks = sum(self.subject_marks_dict.values())
        num_subjects = len(self.subject_marks_dict)

        if num_subjects == 0:
            return 0

        average = total_marks / num_subjects
        return average
