
from utils import(  get_non_empty_input,
                    get_float_input,
                    get_int_input,
                    get_confirmation,
                    get_valid_doctor_id,
                    get_available_room_number,
                    get_valid_email,
                    get_valid_date,
                    get_valid_gender,
                    statistics_menu,
                    get_valid_phone    ) 

#------------------------------> import hospital.py ----------------------------

from hospital import Hospital

#-----------------------------> import doctor.py -------------------------------

from doctor import Doctor

#-----------------------------> import employee.py -----------------------------

from employee import Employee

#-----------------------------> import patient.py ------------------------------
from patient import Patient


#-----------------------------> Objects ----------------------------------------

hospital = Hospital(hospital_id=12,
                    hospital_name='Punjab Hospital',
                    location='Lahore'   )
hospital.load_data()

# ------------------------------------------------------------------------------

doctor1 = Doctor(   doctor_id=101,name='Ahmad',age=45,gender='Male',
                    specialization='Cardiologist',phone='03026633383',email='iamfaizii@gmail.com',
                    salary=10000,department='Cardiology'   )



doctor2 = Doctor(   doctor_id=204,name='Adam',age=56,gender='Male',specialization='Dentist',
                    phone='028475654',email='adam@gmail.com',salary=20000,department="Dental"   )

# ------------------------------------------------------------------------------------

employee = Employee(    employee_id=303,name='Ali',age=34,gender='Male',job_title='Nurse',phone='03001234567',
                        email='ali786@gmail.com',salary=40000,department='Emergency')

# -------------------------------------------------------------------------------------

patient = Patient(      patient_id=100,name='asim',age=23,gender='male',phone='03027294223',
                        email='asimkhan@gmail.com',address='Lahore',joining_date='28-sep-2026',
                        discharge_date=None,disease='dengue fever',doctor_id=101,room_number=5005     )


# ----------------->  Hospital Management System Menu ----------------------------------

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

                    phone = get_valid_phone("Enter Doctor Phone Number: ")

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

                    phone = get_valid_phone("Enter Employee Phone Number: ")

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

                    phone = get_valid_phone("Enter Patient Phone Number: ")

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

        while True:


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

                statistics_menu(hospital)


            elif user_input == '0':

                print('Back To Menu. ')
                break

            else:
                print('InValid Choice. ')


    elif user_input == '0':
        print("Exit")
        break

    else:
        print("InValid Choice: ")
        
