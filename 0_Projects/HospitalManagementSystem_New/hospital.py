
from utils import (
    get_int_input,
    get_float_input,
    get_confirmation,
    get_valid_doctor_id,
    get_available_room_number,
    get_non_empty_input,
)

# ------------------------ Hospital Class -------------------------

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


# ----> Doctors CRUD Method ------------------



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

                new_salary = get_float_input("Enter New Salary: ")
                doctor.salary = new_salary
                print('Doctor salary updated successfully.')


            elif user_input == '2':
                new_phone = input("Enter New Phone Number: ")
                doctor.phone = new_phone
                print('Doctor phone number updated successfully.')

            elif user_input == '3':
                new_email = input("Enter New Email: ")
                doctor.email = new_email
                print('Doctor email updated successfully.')

            elif user_input == '4':
                new_name = input("Enter New Name: ")
                doctor.name = new_name
                print('Doctor name updated successfully.')

            elif user_input == '5':


                new_age = get_int_input("Enter New Age: ")
                doctor.age = new_age
                print('Doctor age updated successfully.')

            elif user_input == '6':
                new_department = input("Enter New Department: ")
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

                if get_confirmation('Are you sure you want to delete this doctor? (yes/no):---> '):

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

                



# ----> Employee CRUD Method -----------------------


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

                new_salary = get_float_input("Enter New Salary: ")
                employee.salary = new_salary
                print('Employee salary updated successfully.')

            elif user_input == '2':
                new_phone = input("Enter New Phone Number: ")
                employee.phone = new_phone
                print("Employee Phone Number updated successfully.")

            elif user_input == '3':
                new_email = input("Enter New Email: ")
                employee.email = new_email
                print('Employee Email updated successfully.')

            elif user_input == '4':
                new_name = input("Enter New Name: ")
                employee.name = new_name
                print('Employee Name updated successfully.')

            elif user_input == '5':

                new_age = get_int_input("Enter New Age: ")
                employee.age = new_age
                print('Employee age updated successfully.')

            elif user_input == '6':
                new_department = input("Enter New Department: ")
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

                if get_confirmation('Are you sure you want to delete this Employee? (yes/no):----->  '):

                    del self.employees[employee_id]
                    print(f'Employee {employee_id} deleted successfully.')

                else:
                    print('Employee deletion cancelled.')
            else:
                print(f'Employee {employee_id} Not Found: ')
        


# ----->  PATIENT CRUD METHOD ------------------------


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
                new_name = input("Enter New Name: ")
                patient.name = new_name
                print('Patient Name updated successfully. ')

            elif user_input == '2':

                new_age = get_int_input("Enter New Age: ")
                patient.age = new_age
                print('Patient age updated successfully.')

            elif user_input == '3':
                new_phone = input("Enter New Phone Number: ")
                patient.phone = new_phone
                print('Patient Phone_Number updated successfully. ')

            elif user_input == '4':
                new_email = input('Enter New Email: ')
                patient.email = new_email
                print('Patient Email updated successfully. ')

            elif user_input ==  '5':
                discharge_date = input("Enter Discharge Date: ")
                patient.discharge_date = discharge_date
                print('Patient Discharge_Date updated successfully. ')

            elif user_input == '6':
                new_disease = input("Enter New Disease: ")
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

            if get_confirmation('Are you sure you want to delete this Patient? (yes/no):----->  '):

                del self.patients[patient_id]
                print(f'Patient {patient_id} deleted successfully. ')

            else:
                print('Patient deletion cancelled. ')

        else:
            print(f'Patient {patient_id} Not Found: ')


