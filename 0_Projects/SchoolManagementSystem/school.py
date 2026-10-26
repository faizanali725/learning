
# ---------------------> SCHOOL CLASS <---------------------

class School:

    def __init__(self,school_name:str,school_address:str,school_phone_number:str,school_email:str):
        self.school_name = school_name
        self.school_address = school_address
        self.school_phone_number = school_phone_number
        self.school_email = school_email
        self.students = {}
        self.teachers = {}
        self.employees = {}



    def display_info(self):
        print(f"School Name: {self.school_name}")
        print(f"School Address: {self.school_address}")
        print(f"School Phone Number: {self.school_phone_number}")
        print(f"School Email: {self.school_email}")




# --------------------> STUDENT CRUD METHOD <---------------------




# --------------------> Create Student Method <---------------------


    def add_student(self,student):

        if student.student_id in self.students:
            print(f"Student with ID {student.student_id} already exists.")

        else:
            self.students[student.student_id] = student
            print(f"Student {student.student_id} added successfully.")


# --------------------> Read Student Method <---------------------


    def view_students(self):
    
        if not self.students:
            print("Students Not found.")
        else:
            for stu in self.students.values():
                stu.display_info()



# ---------------------> Update Student Method <---------------------


    def update_student(self,student_id):

        if student_id in self.students:
            print(f"Student with ID {student_id} Found successfully.")

            student = self.students[student_id]

            user_input = input("""
                        
                            Hello, Which information do you want to update?

                            1. Enter 1 to Update Student Name
                            2. Enter 2 to Update Student Age
                            3. Enter 3 to Update Student Phone Number
                            4. Enter 4 to Update Student Class
                            5. Enter 5 to Update Student Email
                            6. Enter 6 to Update Student Marks

                            0. Enter 0 to Update Cancelled 

                            Enter your Choice:
""")


            if user_input == "1":

                new_name = input("Enter New Name: ")
                student.name = new_name
                print("Student Name Updated Successfully.")


            elif user_input == "2":

                new_age = int(input("Enter New Age: "))
                student.age = new_age
                print("Student Age Updated Successfully.")


            elif user_input == '3':

                new_phone_number = input("Enter New Phone Number: ")
                student.phone_number = new_phone_number
                print("Student Phone Number Updated Successfully.")


            elif user_input == '4':

                new_class = input("Enter New Class: ")
                student.class_name = new_class
                print("Student Class Updated Successfully.")


            elif user_input == '5':

                new_email = input("Enter New Email: ")
                student.email = new_email
                print("Student Email Updated Successfully.")


            elif user_input == '6':

                new_marks = int(input("Enter New Marks: "))
                student.marks = new_marks
                print("Student Marks Updated Successfully.")


            elif user_input == '0':

                print("Update Cancelled.")

            else:
                print("Invalid Choice. Please try again.")


# --------------------> Delete Student Method <---------------------


    def delete_student(self,student_id):
    
        if student_id in self.students:
            print(f"Student with ID {student_id} Found successfully.")

            confirmed = input("Are you sure you want to delete this student? (yes/no): ").lower()
            if confirmed == "yes":
                del self.students[student_id]
                print(f"Student with ID {student_id} deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Student with ID {student_id} not found.")





# ---------------------------> TEACHER CRUD METHOD <--------------------------




# ---------------------------> Create Teacher Method <-------------------------


    def add_teacher(self,teacher):

        if teacher.teacher_id in self.teachers:
            print(f"Teacher With ID {teacher.teacher_id} already exist. ")

        else:
            self.teachers[teacher.teacher_id] = teacher
            print(f"Teacher {teacher.teacher_id} Added successfully. ")


# ---------------------------> Read Teacher Method <--------------------------


    def view_teachers(self):

        if not self.teachers:
            print("Teachers Not Found. ")

        else:
            for teach in self.teachers.values():
                teach.display_info()



# --------------------------> Update Teacher Method <---------------------------


    def update_teacher(self,teacher_id):

        if teacher_id in self.teachers:
            print(f"Teacher with ID {teacher_id} Found successfully.")

            teacher = self.teachers[teacher_id]

            user_input = input("""
                        
                            Hello, Which information do you want to update?

                            1. Enter 1 to Update Teacher Salary
                            2. Enter 2 to Update Teacher Name
                            3. Enter 3 to Update Teacher Age
                            4. Enter 4 to Update Teacher Email
                            5. Enter 5 to Update Teacher Phone Number
                            6. Enter 6 to Update Teacher Subject

                            0. Enter 0 to Update Canceled

                            Enter your Choice: 

""")

            if user_input == '1':

                new_salary = int(input("Enter New Salary: "))
                teacher.salary = new_salary
                print("Teacher Salary updated successfully. ")


            elif user_input == '2':

                new_name = input("Enter New Name: ")
                teacher.name = new_name
                print("Teacher Name updated successfully. ")


            elif user_input == '3':

                new_age = int(input("Enter New Age: "))
                teacher.age = new_age
                print("Teacher Age updated successfully. ")


            elif user_input == '4':

                new_email = input("Enter New Email: ")
                teacher.email = new_email
                print("Teacher Email updated successfully. ")


            elif user_input == '5':

                new_phone_number = input("Enter New Phone Number: ")
                teacher.phone_number = new_phone_number
                print("Teacher Phone Number updated successfully. ")


            elif user_input == '6':

                new_subject = input("Enter New Subject: ")
                teacher.subject = new_subject
                print("Teacher Subject updated successfully. ")


            elif user_input == '0':

                print("Update Canceled")

            else:
                print("InValid Choice: Please Try Again. ")

        else:
            print(f"Teacher With ID {teacher_id} Not Found. ")



# --------------------------> Delete Teacher Method <---------------------------


    def delete_teacher(self,teacher_id):

        if teacher_id in self.teachers:

            print(f"Teacher With ID {teacher_id} Found successfully. ")

            confirmed = input("Are you sure you want to delete this Teacher? (yes/no): ").lower()

            if confirmed == 'yes':
                del self.teachers[teacher_id]
                print(f"Teacher with ID {teacher_id} deleted successfully.")

            else:
                print("Deletion cancelled.")

        else:
            print(f"Teacher With ID {teacher_id} Not Found. ")




# -----------------------------> EMPLOYEE CRUD METHOD <----------------------------



# -----------------------------> Create Employee Method <-----------------------------


    def add_employee(self,employee):

        if employee.employee_id in self.employees:
            print(f"Employee With ID {employee.employee_id} already exist. ")

        else:
            self.employees[employee.employee_id] = employee
            print(f"Employee {employee.employee_id} Added successfully. ")



# ----------------------------> Read Employee Method <--------------------------------


    def view_employees(self):

        if not self.employees:
            print("Employee not Found. ")

        else:
            for emp in self.employees.values():
                emp.display_info()



# -----------------------------> Update Employee Method <----------------------------


    def update_employee(self,employee_id):
        
        if employee_id in self.employees:
            print(f"Employee With ID {employee_id} Found successfully. ")

            employee = self.employees[employee_id]

            user_input = input("""

                            Hello, Which information do you want to update?

                            1. Enter 1 to Update Employee Salary
                            2. Enter 2 to Update Employee Name
                            3. Enter 3 to Update Employee Age
                            4. Enter 4 to Update Employee Email
                            5. Enter 5 to Update Employee Phone Number

                            0. Enter 0 to Cancelled Update

                            Enter your Choice: 
""")

            if user_input == '1':

                new_salary = int(input("Enter New Salary: "))
                employee.salary = new_salary
                print(f"Employee Salary updated successfully. ")


            elif user_input == '2':

                new_name = input("Enter New Name: ")
                employee.name = new_name
                print(f"Employee Name updated successfully. ")


            elif user_input == '3':

                new_age = int(input("Enter New Age: "))
                employee.age = new_age
                print(f"Employee Age updated successfully. ")


            elif user_input == '4':

                new_email = input("Enter New Email: ")
                employee.email = new_email
                print(f"Employee Email updated successfully. ")


            elif user_input == '5':

                new_phone_number = input("Enter New Phone Number: ")
                employee.phone_number = new_phone_number
                print(f"Employee Phone Number updated successfully. ")



            elif user_input == '0':

                print("Update Cancelled")


            else:
                print("InValid Choice: Please Try Again. ")

                
        else:
            print(f"Employee with ID {employee_id} Not Found. ")


# -----------------------------> Delete Employee Method <-------------------------------


    def delete_employee(self,employee_id):

        if employee_id in self.employees:
            print(f"Employee With ID {employee_id} Found successfully. ")

            confirmed = input("Are you sure you want to delete this Employee? (yes/no): ").lower()

            if confirmed == 'yes':
                del self.employees[employee_id]
                print(f"Employee with ID {employee_id} deleted successfully.")

            else:
                print("Deletion Canceled")

        else:
            print(f"Employee with ID {employee_id} Not Found. ")

