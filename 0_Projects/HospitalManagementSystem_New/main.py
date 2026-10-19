
from utils import(get_non_empty_input,
                    get_float_input,
                    get_int_input,
                    get_confirmation,
                    get_valid_doctor_id,
                    get_available_room_number,
                    get_valid_email,
                    get_valid_date,
                    get_valid_gender,   ) 



class Hospital:

    def __init__(self,hospital_id:int,hospital_name:str,location:str):
        self.hospital_id = hospital_id
        self.hospital_name = hospital_name
        self.location = location
        self.doctors = {}
        self.employees = {}
        self.patients = {}


    def display_info(self):
            
        print('Hospital ID: ',self.hospital_id)
        print('Hospital Name: ',self.hospital_name)
        print('Hospital Location: ',self.location)


    def hospital_statistics(self):

            user_input = input("""

                        ========== HOSPITAL STATISTICS ==========

                       1. Total Doctors
                       2. Total Employees
                       3. Total Patients

                       Enter your Choice. 

""")
            if user_input == '1':
                doc = len(self.doctors)
                print('Total Doctors: ',doc)

            elif user_input == '2':
                emp = len(self.employees)
                print('Total Employees: ',emp)

            elif user_input == '3':
                pat = len(self.patients)
                print('Total Patients: ',pat)

            else:
                print('InValid Choice: ')

# ----> Doctors CRUD Method

# Add Doctor

    def add_doctor(self,doctor):
    
         if doctor.doctor_id in self.doctors:
                print(f'Doctor with ID {doctor.doctor_id} already exists.')
         else:
            self.doctors[doctor.doctor_id] = doctor
            print(f'Doctor {doctor.doctor_id} added successfully.')
                

    
# View Doctors

    def view_doctors(self):
        if not self.doctors:
            print("Not Found Doctor")

        else:
            for doc in self.doctors.values():
                doc.display_info()



# Update Doctor


    def update_doctor(self,doctor_id):
        if doctor_id in self.doctors:

            print(f"Doctor with ID {doctor_id} found successfully.")

            doctor = self.doctors[doctor_id]


            user_input = input("""
                        Hello, Which information do you want to update?

                        1. Enter 1 to Update Salary
                        2. Enter 2 to Update Phone No
                        3. Enter 3 to Update Email 
                        4. Enter 4 to Update Name
                        5. Enter 5 to Update Age
                        6. Enter 6 to Update Department

                        0. Enter 0 for Update Cancelled

                        Enter your choice: 
""")

            if user_input == '1':

                new_salary = get_float_input("Enter New Salary: ", min_value = 0)
                doctor.salary = new_salary
                print('Doctor salary updated successfully.')


            elif user_input == '2':
                new_phone = get_non_empty_input("Enter New Phone Number: ")
                doctor.phone = new_phone
                print('Doctor phone number updated successfully.')

            elif user_input == '3':
                new_email = get_valid_email("Enter New Email: ")
                doctor.email = new_email
                print('Doctor email updated successfully.')

            elif user_input == '4':
                new_name = get_non_empty_input("Enter New Name: ")
                doctor.name = new_name
                print('Doctor name updated successfully.')

            elif user_input == '5':

                new_age = get_int_input("Enter New Age: ", min_value = 1)
                doctor.age = new_age
                print('Doctor age updated successfully.')

            elif user_input == '6':

                new_department = get_non_empty_input("Enter New Department: ")
                doctor.department = new_department
                print('Doctor department updated successfully.')

            elif user_input == '0':
                print('Update Doctor Cancelled')
            else:
                print('Invalid Choice')
        else:
            print('Doctor not found')


# Delete Doctor
    def delete_doctor(self,doctor_id):
            
            if doctor_id in self.doctors:

                print(f"Doctor with ID {doctor_id} found successfully.")

                confirmed = get_confirmation('Are you sure you want to delete this doctor? (yes/no):---> ')

                if confirmed:

                        for patient in self.patients.values():

                            if doctor_id == patient.doctor_id:

                                print("Doctor cannot be deleted because this doctor is assigned to a patient.")
                                return
                                

                    
                        del self.doctors[doctor_id]
                        print('Doctor deleted successfully.')
                                
                else:
                    print('Doctor deletion cancelled.')
            else:
                print('Doctor not found')

                



# ----> Employee CRUD Method 

# Add Employee
    def add_employee(self,employee):

        if employee.employee_id in self.employees:
            print(f'Employee with ID  {employee.employee_id} already exists')
        else:
            self.employees[employee.employee_id] = employee
            print(f'Employee {employee.employee_id} added successfully')

# View Employees
    def view_employees(self):
        if not self.employees:
            print("Not Found Employee")
        
        else:
            for emp in self.employees.values():
                emp.display_info()

# Update Employee

    def update_employee(self,employee_id):
        if employee_id in self.employees:
            print(f"Employee with ID {employee_id} found successfully.")

            employee = self.employees[employee_id]

            user_input = input(""" 
                        Hello, Which information do you want to update?

                        1.  Enter 1 to Update Salary
                        2.  Enter 2 to Update Phone Number
                        3.  Enter 3 to Update Email
                        4.  Enter 4 to Update Name
                        5.  Enter 5 to Update Age
                        6.  Enter 6 to Update Department

                        0.  Enter 0 to Cancel Update

                        Enter your choice:

""")

            if user_input == '1':

                new_salary = get_float_input("Enter New Salary: ", min_value = 0)
                employee.salary = new_salary
                print('Employee salary updated successfully.')

            elif user_input == '2':
                new_phone = get_non_empty_input("Enter New Phone Number: ")
                employee.phone = new_phone
                print("Employee Phone Number updated successfully.")

            elif user_input == '3':
                new_email = get_valid_email("Enter New Email: ")
                employee.email = new_email
                print('Employee Email updated successfully.')

            elif user_input == '4':
                new_name = get_non_empty_input("Enter New Name: ")
                employee.name = new_name
                print('Employee Name updated successfully.')

            elif user_input == '5':

                new_age = get_int_input("Enter New Age: ", min_value = 1)
                employee.age = new_age
                print('Employee Age updated successfully.')

            elif user_input == '6':
                new_department = get_non_empty_input("Enter New Department: ")
                employee.department = new_department
                print('Employee Department updated successfully.')

            elif user_input == '0':
                print('Update Employee Cancelled')

            else:
                print("InValid Choice. ")
        else:
            print(f"Employee {employee_id} NOt Found. ")


#  Delete Employee

    def delete_employee(self,employee_id):
        
            if employee_id in self.employees:
        
                print(f"Employee with ID {employee_id} found successfully.")

                confirmed = get_confirmation('Are you sure you want to delete this Employee? (yes/no):----->  ')

                if confirmed:

                    del self.employees[employee_id]
                    print(f'Employee {employee_id} deleted successfully.')

                else:
                    print('Employee deletion cancelled.')
            else:
                print(f'Employee {employee_id} Not Found: ')
        


# ----->  PATIENT CRUD METHOD 


# Add Patient

    def add_patient(self,patient):

        if patient.patient_id in self.patients:
            print(f'Patient with ID {patient.patient_id} already exists.')
        else:
            self.patients[patient.patient_id] = patient
            print(f'Patient {patient.patient_id} added successfully.')

#  View Patient

    def view_patients(self):
        if not self.patients:
            print("Patient Not Found: ")
        else:
            for pat in self.patients.values():
                pat.display_info(self.doctors)


#  Update Patient

    def update_patient(self,patient_id):
        if patient_id in self.patients:
            print(f'Patient With ID {patient_id} found successfully: ')

            patient = self.patients[patient_id]

            user_input = input("""
                        Hello, Which information do you want to update?

                        1. Enter 1 to Update Name
                        2. Enter 2 to Update Age
                        3. Enter 3 to Update Phone Number
                        4. Enter 4 to Update Email
                        5. Enter 5 to Update Discharge Date
                        6. Enter 6 to Update Disease
                        7. Enter 7 to Update Doctor ID
                        8. Enter 8 to Update Room Number

                        0. Enter 0 to Cancel Update

                        Enter your choice:
""")

            if user_input == '1':
                new_name = get_non_empty_input("Enter New Name: ")
                patient.name = new_name
                print('Patient Name updated successfully. ')

            elif user_input == '2':

                new_age = get_int_input("Enter New Age: ", min_value = 1)
                patient.age = new_age
                print("Patient Age updated successfully. ")

            elif user_input == '3':
                new_phone = get_non_empty_input("Enter New Phone Number: ")
                patient.phone = new_phone
                print('Patient Phone_Number updated successfully. ')

            elif user_input == '4':
                new_email = get_valid_email("Enter New Email: ")
                patient.email = new_email
                print('Patient Email updated successfully. ')

            elif user_input ==  '5':
                discharge_date = get_non_empty_input("Enter Discharge Date: ")
                patient.discharge_date = discharge_date
                print('Patient Discharge_Date updated successfully. ')

            elif user_input == '6':
                new_disease = get_non_empty_input("Enter New Disease: ")
                patient.disease = new_disease
                print('Patient Disease updated successfully. ')

            elif user_input == '7':

                new_doctor_id = get_valid_doctor_id("Enter New Doctor ID: ", self.doctors)
                if new_doctor_id is not None:
                    patient.doctor_id = new_doctor_id
                    print('Patient Doctor ID updated successfully. ')

            elif user_input == '8':

                new_room_number = get_available_room_number(
                    "Enter New Room Number: ",
                    self.patients,
                    current_patient_id=patient_id
                )
                patient.room_number = new_room_number
                print('Patient Room Number updated successfully. ')

            elif user_input == '0':
                print('Update Patient Cancelled. ')

            else:
                print('InValid Choice: ')

        else:
            print(f'Patient {patient_id} Not Found: ')


# Delete Patient

    def delete_patient(self,patient_id):
        if patient_id in self.patients:
            print(f'Patient With ID {patient_id} Found successfully. ')

            confirmed = get_confirmation('Are you sure you want to delete this Patient? (yes/no):----->  ')

            if confirmed:

                del self.patients[patient_id]
                print(f'Patient {patient_id} deleted successfully. ')

            else:
                print('Patient deletion cancelled. ')

        else:
            print(f'Patient {patient_id} Not Found: ')




# ---------------- Doctor Class ------------------------

class Doctor:

    def __init__(self,doctor_id:int,name:str,age:int,gender:str,specialization:str,phone:str
,email:str,salary:float,department:str):
        self.doctor_id = doctor_id
        self.name = name
        self.age = age
        self.gender = gender
        self.specialization = specialization
        self.phone = phone
        self.email = email
        self.salary = salary 
        self.department = department

    def display_info(self):
        print('Doctor_id: ',self.doctor_id)
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Specialization: ',self.specialization)
        print('Phone_No: ',self.phone)
        print('Gender: ',self.gender)
        print('Email: ',self.email)
        print('Salary: ',self.salary)
        print('Department: ',self.department)



# ---------------- Employee Class ------------------------

class Employee:

    def __init__(self,employee_id:int,name:str,age:int,gender:str,job_title:str,phone:str,email:str,salary:float,department:str):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.gender = gender
        self.job_title = job_title
        self.phone = phone
        self.email = email
        self.salary = salary
        self.department = department


    def display_info(self):
        print(f'Employee_ID:  {self.employee_id}')
        print(f'Name:  {self.name}')
        print(f'Age:  {self.age}')
        print(f'Gender:  {self.gender}')
        print(f'Job_title:  {self.job_title}')
        print(f'Phone:  {self.phone}')
        print(f'Email:  {self.email}')
        print(f'Salary:  {self.salary}')
        print(f'Department:  {self.department}')


# ------------------------ Patient Class -------------------------

class Patient:

    def __init__(self,patient_id:int,name:str,age:int,gender:str,phone:str,email:str,address:str,joining_date:str,discharge_date:str,disease:str,doctor_id:int,room_number:int):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address
        self.joining_date = joining_date
        self.discharge_date = discharge_date
        self.disease = disease
        self.doctor_id = doctor_id
        self.room_number = room_number


    def display_info(self,doctors):
        print(f'Patient_ID:  {self.patient_id}')
        print(f'Name:  {self.name}')
        print(f'Age:  {self.age}')
        print(f'Gender:  {self.gender}')
        print(f'Phone:  {self.phone}')
        print(f'Email:  {self.email}')
        print(f'Address:  {self.address}')
        print(f'Joining_Date:  {self.joining_date}')
        print(f'Discharge_Date:  {self.discharge_date}')
        print(f'Disease:  {self.disease}')
        print(f'Doctor_ID:  {self.doctor_id}')
        if self.doctor_id in doctors:
            doctor = doctors[self.doctor_id]
            print(f'Doctor Name: {doctor.name}')
            print(f'Doctor Specialization: {doctor.specialization}')
            print(f'Doctor Department: {doctor.department}')
        else:
            print('Doctor information not available. ')
        print(f'Room_Number:  {self.room_number}')
        
        


# Objects

hospital = Hospital(hospital_id=12,hospital_name='Punjab Hospital',location='Lahore')

# -------------------------------------------

doctor1 = Doctor(doctor_id=101,name='Ahmad',age=45,gender='Male',specialization='Cardiologist',phone='03026633383',email='iamfaizii@gmail.com',salary=10000,department='Cardiology')
doctor2 = Doctor(doctor_id=204,name='Adam',age=56,gender='Male',specialization='Dentist',phone='028475654',email='adam@gmail.com',salary=20000,department="Dental")

# -------------------------------------------

employee = Employee(employee_id=303,name='Ali',age=34,gender='Male',job_title='Nurse',phone='03001234567',email='ali786@gmail.com',salary=40000,department='Emergency')

# -------------------------------------------

patient = Patient(patient_id=100,name='asim',age=23,gender='male',phone='03027294223',email='asimkhan@gmail.com',address='Lahore',joining_date='28-sep-2026',discharge_date=None,disease='dengue fever',doctor_id=101,room_number=5005)

# -------------------------------------------

# hospital.display_info()

# print('--------------------------------')

# hospital.add_doctor(doctor=doctor1)
# hospital.add_doctor(doctor=doctor2)

# print('--------------------------------')

# hospital.view_doctors()

# print('--------------------------------')

# hospital.add_employee(employee=employee)

# print('--------------------------------')

# hospital.view_employees()

# print('---------------------------------')

# hospital.add_patient(patient=patient)

# print('----------------------------------)

# hospital.view_patients()

# ----->  Hospital Management System Menu
while True:

    user_input = input("""
                ========== HOSPITAL MANAGEMENT SYSTEM ==========

                1. Doctor Management
                2. Employee Management
                3. Patient Management
                4. Hospital Information

                0. Exit

                Enter Your Choice: 

""")
    if user_input == '1':

        while True:

            user_input = input("""
                         ========== DOCTOR MANAGEMENT SYSTEM =========

                        1.  Add Doctor
                        2.  View Doctor
                        3.  Update Doctor
                        4.  Delete Doctor

                        0.  Back to Menu
 
                        Enter your Choice: 

""")
            if user_input == '1':
                doctor_id = get_int_input("Enter Doctor ID: ", min_value = 1)

                if doctor_id in hospital.doctors:
                    print(f'Doctor with ID  {doctor_id} already exists')

                else:
                    name = get_non_empty_input("Enter Name: ")
                    age = get_int_input("Enter Age: ", min_value = 1)

                    gender = get_valid_gender("Enter Doctor Gender: ")

                    specialization = get_non_empty_input("Enter Doctor Specialization: ")

                    phone = get_non_empty_input("Enter Doctor Phone Number: ")

                    email = get_valid_email("Enter Doctor Email: ")

                    salary = get_float_input("Enter Doctor Salary: ", min_value = 0)

                    department = get_non_empty_input("Enter Doctor Department: ")

                    new_doctor = Doctor(doctor_id=doctor_id,name=name,age=age,gender=gender,specialization=specialization,phone=phone,email=email,salary=salary,department=department)
                        
                    hospital.add_doctor(doctor=new_doctor)


            elif user_input == '2':
                hospital.view_doctors()


            elif user_input == '3':
                doctor_id = get_int_input("Enter Doctor ID: ", min_value = 1)

                hospital.update_doctor(doctor_id=doctor_id)


            elif user_input == '4':

                doctor_id = get_int_input("Enter Doctor ID: ", min_value = 1)
    
                hospital.delete_doctor(doctor_id=doctor_id)

            elif user_input == '0':
                print("Back To Menu: ")
                break

            else:
                print("InValid Choice: ")
        
    elif user_input == '2':

        while True:

            user_input = input("""
                        =========== EMPLOYEE MANAGEMENT SYSTEM ===========

                        1.  Add Employee
                        2.  View Employee
                        3.  Update Employee
                        4.  Delete Employee

                        0.  Back to Menu

                        Enter your Choice: 

""")
            if user_input == '1':

                employee_id = get_int_input("Enter Employee ID:  ", min_value = 1)

                if employee_id in hospital.employees:
                    print(f'Employee with ID  {employee_id} already exists')

                else:
                    name = get_non_empty_input("Enter Employee Name: ")

                    age = get_int_input("Enter Employee Age: ", min_value = 1)

                    gender = get_valid_gender("Enter Employee Gender: ")

                    job_title = get_non_empty_input("Enter Employee job title: ")

                    phone = get_non_empty_input("Enter Employee Phone Number: ")

                    email = get_valid_email("Enter Employee Email: ")

                    salary = get_float_input("Enter Employee Salary: ", min_value = 0)

                    department = get_non_empty_input("Enter Employee Department: ")

                    new_employee = Employee(employee_id=employee_id,name=name,age=age,gender=gender,job_title=job_title,phone=phone,email=email,salary=salary,department=department)

                    hospital.add_employee(employee=new_employee)


            elif user_input == '2':
                hospital.view_employees()

            elif user_input == '3':

                employee_id = get_int_input("Enter Employee ID: ", min_value = 1)

                hospital.update_employee(employee_id=employee_id)

            elif user_input == '4':

                employee_id = get_int_input("Enter Employee ID: ", min_value = 1)

                hospital.delete_employee(employee_id=employee_id)
                

            elif user_input == '0':
                print("Back to Menu: ")
                break
            else:
                print("InValid Choice: ")


    elif user_input == '3':

        while True:


            user_input = input("""

                    =========== PATIENT MANAGEMENT SYSTEM ===========
                    
                        1.  Add Patient
                        2.  View Patient
                        3.  Update Patient
                        4.  Delete Patient

                        0.  Back to Menu
                    
                        Enter your Choice: 

""")

            if user_input == '1':

                patient_id = get_int_input("Enter Patient ID: ", min_value = 1)

                if patient_id in hospital.patients:
                        print(f'Patient with ID  {patient_id} already exists')

                else:

                    name = get_non_empty_input("Enter Patient Name: ")

                    age = get_int_input("Enter Patient Age: ", min_value = 1)

                    gender = get_valid_gender("Enter Patient Gender: ")

                    phone = get_non_empty_input("Enter Patient Phone Number: ")

                    email = get_valid_email("Enter Patient Email: ")

                    address = get_non_empty_input("Enter Patient Address: ")

                    joining_date = get_valid_date("Enter Joining Date (DD-MM-YYYY): ")

                    discharge_date = None

                    disease = get_non_empty_input("Enter Patient Primary Disease: ")

                    doctor_id = get_valid_doctor_id("Enter Doctor ID: ", hospital.doctors)
                    if doctor_id is None:
                        continue


                    room_number = get_available_room_number(
                        "Enter Room Number: ",
                        hospital.patients
                    )




                    new_patient = Patient(patient_id=patient_id,name=name,age=age,gender=gender,phone=phone,email=email,address=address,joining_date=joining_date,discharge_date=discharge_date,disease=disease,doctor_id=doctor_id,room_number=room_number)    

                    hospital.add_patient(patient=new_patient)



            elif user_input == '2':

                hospital.view_patients()

            elif user_input == '3':

                patient_id = get_int_input("Enter Patient ID: ", min_value = 1)
                
                hospital.update_patient(patient_id=patient_id)
                

            elif user_input == '4':
                patient_id = get_int_input("Enter Patient ID: ", min_value = 1)

                hospital.delete_patient(patient_id=patient_id)


            elif user_input == '0':
                print("Back to Menu")
                break

            else:
                print('InValid Choice: ')


            
    elif user_input == '4':

        user_input = input("""
                    ============ HOSPITAL INFORMATION =========

                    1. Hospital Details
                    2. Hospital Statistics

                    0. Back to Menu

                    Enter your Choice. 

""")
        if user_input == '1':

            hospital.display_info()

        elif user_input == '2':

            hospital.hospital_statistics()


        elif user_input == '0':

            print('Back To Menu. ')

        else:
            print('InValid Choice. ')


    elif user_input == '0':
        print("Exit")
        break

    else:
        print("InValid Choice: ")
        
