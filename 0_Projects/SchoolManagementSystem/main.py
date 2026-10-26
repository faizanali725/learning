
# ------------------> Import Student Class <-----------------

from student import Student

# ------------------> Import School Class <-----------------

from school import School

# ------------------> Import Teacher Class <-----------------

from teacher import Teacher

# ------------------> Import Employee Class <-----------------

from employee import Employee



school = School(
    school_name="ABC School",
    school_address="Lahore",
    school_phone_number="0289077159",
    school_email="info@abcschool.com"
)



#  ----------------------------> Main Menu <--------------------------

while True:

    user_input = input("""

                ========== SCHOOL MANAGEMENT SYSTEM ==========

                1. School Information
                2. Student Management
                3. Teacher Management
                4. Employee Management

                0. Exit

                Enter your choice:
            
""")

# -------------------------> School Information <-------------------------
    

    if user_input == '1':

        school.display_info()



# ------------------------> Student Management <--------------------------


    elif user_input == '2':

        while True:

            user_input = input("""
                            
                            ================ STUDENT MANAGEMENT SYSTEM ================

                            1. Enter 1 to Add Student
                            2. Enter 2 to View Students
                            3. Enter 3 to Update Student
                            4. Enter 4 to Delete Student

                            0. Enter 0 to Back to Main Menu

                            Enter your Choice: 

            """)

            if user_input == "1":

                student_id = int(input("Enter Student ID: "))

                if student_id in school.students:
                    print(f"Student with ID {student_id} already exists.")
                    continue

                name = input("Enter Student Name: ")

                father_name = input("Enter Student Father's Name: ")

                age = int(input("Enter Student Age: "))

                gender = input("Enter Student Gender: ")

                class_name = input("Enter Student Class: ")

                email = input("Enter Student Email: ")

                phone_number = input("Enter Student Phone Number: ")

                address = input("Enter Student Address: ")

                marks = int(input("Enter Student Marks: "))

                student1 = Student(
                    student_id = student_id,
                    name = name,
                    father_name = father_name,
                    age = age,
                    gender = gender,
                    class_name = class_name,
                    email = email,
                    phone_number = phone_number,
                    address = address,
                    marks = marks
                )

                school.add_student(student = student1)


            elif user_input == '2':

                school.view_students()


            elif user_input == '3':

                student_id = int(input("Enter Student ID: "))

                school.update_student(student_id = student_id)


            elif user_input == '4':
                student_id = int(input("Enter Student ID: "))

                school.delete_student(student_id = student_id)


            elif user_input == '0':
                print('Back To Main Menu')
                break

            else:
                print('InValid Choice: Please Try Again.')


#  --------------------------> Teacher Management <--------------------------


    elif user_input == '3':

        while True:

            user_input = input("""

                            ================ TEACHER MANAGEMENT SYSTEM ================

                            1. Enter 1 to Add Teacher
                            2. Enter 2 to View Teacher
                            3. Enter 3 to Update Teacher
                            4. Enter 4 to Delete Teacher

                            0. Enter 0 to Back to Main Menu

                            Enter your Choice: 

""")

            if user_input == '1':

                teacher_id = int(input("Enter Teacher ID: "))

                if teacher_id in school.teachers:
                    print(f"Teacher with ID {teacher_id} already exists.")
                    continue

                name = input("Enter Teacher Name: ")

                age = int(input("Enter Teacher Age: "))

                gender = input("Enter Teacher Gender: ")

                subject = input("Enter Teacher Subject: ")

                phone_number = input("Enter Teacher Phone Number: ")

                email = input("Enter Teacher Email: ")

                salary = int(input("Enter Teacher Salary: "))

                teach = Teacher(
                        teacher_id = teacher_id,
                        name = name,
                        age = age,
                        gender = gender,
                        subject = subject,
                        phone_number = phone_number,
                        email = email,
                        salary = salary 
                )

                school.add_teacher(teacher = teach)



            elif user_input == '2':

                school.view_teachers()


            elif user_input == '3':

                teacher_id = int(input("Enter Teacher ID: "))

                school.update_teacher(teacher_id = teacher_id)


            elif user_input == '4':

                teacher_id = int(input("Enter Teacher ID: "))

                school.delete_teacher(teacher_id = teacher_id)


            elif user_input == '0':

                print("Back to Main Menu")
                break

            else:
                print("InValid Choice: Please Try Again.")


# -----------------------------------> EMPLOYEE MANAGEMENT <-----------------------------


    elif user_input == '4':

        while True:

            user_input = input("""

                        ================ EMPLOYEE MANAGEMENT SYSTEM ================

                            1. Enter 1 to Add Employee
                            2. Enter 2 to View Employee
                            3. Enter 3 to Update Employee
                            4. Enter 4 to Delete Employee

                            0. Enter 0 to Back to Main Menu

                            Enter your Choice: 

""")

            if user_input == '1':

                employee_id = int(input("Enter Employee ID: "))
                
                if employee_id in school.employees:
                    print(f"Employee with ID {employee_id} already exists.")
                    continue
                
                name = input("Enter Employee Name: ")
                
                age = int(input("Enter Employee Age: "))
                
                gender = input("Enter Employee Gender: ")
                
                job_title = input("Enter Job_Title: ")
                
                phone_number = input("Enter Employee Phone Number: ")
                
                email = input("Enter Employee Email: ")
                
                salary = int(input("Enter Employee Salary: "))
                
                employee = Employee(
                            employee_id = employee_id,
                            name = name,
                            age = age,
                            gender = gender,
                            job_title = job_title,
                            phone_number = phone_number,
                            email = email,
                            salary = salary
                )
                
                school.add_employee(employee = employee)


            elif user_input == '2':

                school.view_employees()


            elif user_input == '3':

                employee_id = int(input("Enter Employee ID: "))

                school.update_employee(employee_id = employee_id)


            elif user_input == '4':

                employee_id = int(input("Enter Employee ID: "))

                school.delete_employee(employee_id = employee_id)


            elif user_input == '0':

                print("Back to Main Menu. ")
                break

            else:
                print("InValid Choice: Please Try Again. ")
                


# ----------------------> Exit Program <----------------------

    elif user_input == '0':

        print('Exit')
        break


    else:
        print("InValid Choice: Please Try Again.")




                

                