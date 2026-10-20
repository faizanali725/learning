
import json


from doctor import Doctor
from employee import Employee
from patient import Patient



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
                    get_valid_phone   ) 




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




    def save_data(self):
        data = {
                "doctors": {
                        doc_id: doc.to_dict() 
                        for doc_id, doc in self.doctors.items()
                    },

                "employees": {
                        emp_id: emp.to_dict()
                        for emp_id, emp in self.employees.items()
                    },

                "patients": {
                        pat_id: pat.to_dict()
                        for pat_id, pat in self.patients.items()
                    }
            }

        with open("hospital_data.json", "w") as f:
            json.dump(data, f, indent=4)

    
    
    def load_data(self):
        import math
        from datetime import datetime

        # Detect duplicate keys inside the JSON file
        class DuplicateJSONKeyError(Exception):
            pass

        def reject_duplicate_keys(pairs):
            result = {}

            for key, value in pairs:
                if key in result:
                    raise DuplicateJSONKeyError(
                        f"Duplicate JSON key: {key}"
                    )
                result[key] = value

            return result

        # ---------- Validation helpers ----------

        def require_text(record, field):
            value = record[field]

            if not isinstance(value, str) or not value.strip():
                raise ValueError(
                    f"{field} must be a non-empty string"
                )

            return value.strip()

        def require_id(record, field):
            value = record[field]

            if type(value) is not int or value < 1:
                raise ValueError(
                    f"{field} must be a positive integer"
                )

            return value

        def require_age(record):
            value = record["Age"]

            if type(value) is not int or value < 1:
                raise ValueError(
                    "Age must be a positive integer"
                )

            return value

        def require_salary(record):
            value = record["Salary"]

            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or value < 0
            ):
                raise ValueError(
                    "Salary must be a finite, non-negative number"
                )

            return value

        def require_gender(record):
            value = require_text(record, "Gender")

            if value.casefold() not in (
                "male", "female", "m", "f"
            ):
                raise ValueError("Invalid gender")

            return value

        def require_phone(record, field):
            value = record[field]

            # Support numeric values from older JSON files too.
            # Store phone numbers as strings to preserve leading zeros.
            if type(value) is int and value >= 0:
                value = str(value)

            if (
                not isinstance(value, str)
                or not value.isdigit()
            ):
                raise ValueError(
                    f"{field} must contain digits only"
                )

            return value

        def require_email(record):
            email = require_text(record, "Email")
            parts = email.split("@")

            if (
                len(parts) != 2
                or not parts[0]
                or "." not in parts[1]
                or parts[1].startswith(".")
                or parts[1].endswith(".")
                or any(char.isspace() for char in email)
            ):
                raise ValueError("Invalid email format")

            return email

        def require_date(value, field, optional=False):
            if optional and value is None:
                return None

            if not isinstance(value, str):
                raise ValueError(
                    f"{field} must be a date in DD-MM-YYYY format"
                )

            try:
                parsed_date = datetime.strptime(
                    value, "%d-%m-%Y"
                )

                # Reject non-padded dates such as 1-2-2026.
                if parsed_date.strftime("%d-%m-%Y") != value:
                    raise ValueError

            except ValueError:
                raise ValueError(
                    f"{field} must be a valid date in DD-MM-YYYY format"
                )

            return value

        def check_record_key(json_key, record_id, entity):
            if json_key != str(record_id):
                raise ValueError(
                    f"JSON key {json_key!r} does not match "
                    f"the {entity} ID {record_id}"
                )

        # ---------- Read JSON safely ----------

        try:
            with open("hospital_data.json", "r", encoding="utf-8") as f:
                data = json.load(
                    f,
                    object_pairs_hook=reject_duplicate_keys
                )

        except FileNotFoundError:
            print(
                "No existing data found. "
                "Starting with an empty hospital database."
            )
            return

        except json.JSONDecodeError as e:
            print(f"Invalid JSON file: {e}")
            return

        except DuplicateJSONKeyError as e:
            print(f"Duplicate key in JSON file: {e}")
            return

        except OSError as e:
            print(f"Could not read hospital_data.json: {e}")
            return

        if not isinstance(data, dict):
            print("Invalid JSON structure. Expected a dictionary.")
            return

        # Load into temporary dictionaries first.
        # Existing hospital data won't be partially overwritten.
        doctors = {}
        employees = {}
        patients = {}

        # ---------- Load Doctors ----------

        doctors_data = data.get("doctors", {})

        if not isinstance(doctors_data, dict):
            print("Invalid doctors section. Skipping doctors.")
            doctors_data = {}

        for doc_key, doc_data in doctors_data.items():
            try:
                if not isinstance(doc_data, dict):
                    raise ValueError(
                        "Doctor record must be a dictionary"
                    )

                doctor_id = require_id(
                    doc_data, "Doctor_id"
                )
                check_record_key(
                    doc_key, doctor_id, "doctor"
                )

                doctor = Doctor(
                    doctor_id=doctor_id,
                    name=require_text(doc_data, "Name"),
                    age=require_age(doc_data),
                    gender=require_gender(doc_data),
                    specialization=require_text(
                        doc_data, "Specialization"
                    ),
                    phone=require_phone(doc_data, "Phone_No"),
                    email=require_email(doc_data),
                    salary=require_salary(doc_data),
                    department=require_text(
                        doc_data, "Department"
                    )
                )

                if doctor_id in doctors:
                    raise ValueError("Duplicate doctor ID")

                doctors[doctor_id] = doctor

            except (KeyError, TypeError, ValueError, OverflowError) as e:
                print(f"Skipping invalid doctor {doc_key}: {e}")

        # ---------- Load Employees ----------

        employees_data = data.get("employees", {})

        if not isinstance(employees_data, dict):
            print("Invalid employees section. Skipping employees.")
            employees_data = {}

        for emp_key, emp_data in employees_data.items():
            try:
                if not isinstance(emp_data, dict):
                    raise ValueError(
                        "Employee record must be a dictionary"
                    )

                employee_id = require_id(
                    emp_data, "Employee_ID"
                )
                check_record_key(
                    emp_key, employee_id, "employee"
                )

                employee = Employee(
                    employee_id=employee_id,
                    name=require_text(emp_data, "Name"),
                    age=require_age(emp_data),
                    gender=require_gender(emp_data),
                    job_title=require_text(
                        emp_data, "Job_title"
                    ),
                    phone=require_phone(emp_data, "Phone"),
                    email=require_email(emp_data),
                    salary=require_salary(emp_data),
                    department=require_text(
                        emp_data, "Department"
                    )
                )

                if employee_id in employees:
                    raise ValueError("Duplicate employee ID")

                employees[employee_id] = employee

            except (KeyError, TypeError, ValueError, OverflowError) as e:
                print(f"Skipping invalid employee {emp_key}: {e}")

        # ---------- Load Patients ----------

        patients_data = data.get("patients", {})

        if not isinstance(patients_data, dict):
            print("Invalid patients section. Skipping patients.")
            patients_data = {}

        occupied_rooms = set()

        for pat_key, pat_data in patients_data.items():
            try:
                if not isinstance(pat_data, dict):
                    raise ValueError(
                        "Patient record must be a dictionary"
                    )

                patient_id = require_id(
                    pat_data, "Patient_ID"
                )
                check_record_key(
                    pat_key, patient_id, "patient"
                )

                name = require_text(pat_data, "Name")
                age = require_age(pat_data)
                gender = require_gender(pat_data)
                phone = require_phone(pat_data, "Phone")
                email = require_email(pat_data)
                address = require_text(pat_data, "Address")

                joining_date = require_date(
                    pat_data["Joining_Date"], "Joining_Date"
                )

                discharge_date = require_date(
                    pat_data.get("Discharge_Date"),
                    "Discharge_Date",
                    optional=True
                )

                disease = pat_data.get("Disease")

                if disease is not None:
                    if not isinstance(disease, str) or not disease.strip():
                        raise ValueError(
                            "Disease must be non-empty text or null"
                        )
                    disease = disease.strip()

                doctor_id = pat_data.get("Doctor_ID")

                if doctor_id is not None:
                    if type(doctor_id) is not int or doctor_id < 1:
                        raise ValueError("Invalid Doctor_ID")

                    if doctor_id not in doctors:
                        raise ValueError(
                            f"Assigned doctor {doctor_id} does not exist"
                        )

                room_number = pat_data.get("Room_Number")

                if room_number is not None:
                    if (
                        isinstance(room_number, bool)
                        or not isinstance(room_number, (int, str))
                        or (
                            isinstance(room_number, int)
                            and room_number < 1
                        )
                        or (
                            isinstance(room_number, str)
                            and not room_number.strip()
                        )
                    ):
                        raise ValueError("Invalid Room_Number")

                    room_key = str(room_number).strip()

                    if room_key in occupied_rooms:
                        raise ValueError(
                            f"Room {room_number} is already assigned"
                        )
                else:
                    room_key = None

                patient = Patient(
                    patient_id=patient_id,
                    name=name,
                    age=age,
                    gender=gender,
                    phone=phone,
                    email=email,
                    address=address,
                    joining_date=joining_date,
                    discharge_date=discharge_date,
                    disease=disease,
                    doctor_id=doctor_id,
                    room_number=room_number
                )

                if patient_id in patients:
                    raise ValueError("Duplicate patient ID")

                patients[patient_id] = patient

                if room_key is not None:
                    occupied_rooms.add(room_key)

            except (KeyError, TypeError, ValueError, OverflowError) as e:
                print(f"Skipping invalid patient {pat_key}: {e}")

        # Replace the dictionaries only after loading finishes.
        self.doctors = doctors
        self.employees = employees
        self.patients = patients

        print(
            "Data loading completed: "
            f"{len(self.doctors)} doctors, "
            f"{len(self.employees)} employees, "
            f"{len(self.patients)} patients loaded."
        )






# ------------------------------> Doctors CRUD Method ----------------------------------

# Add Doctor

    def add_doctor(self,doctor):
    
         if doctor.doctor_id in self.doctors:
                print(f'Doctor with ID {doctor.doctor_id} already exists.')
         else:
            self.doctors[doctor.doctor_id] = doctor
            print(f'Doctor {doctor.doctor_id} added successfully.')

            self.save_data()  # Save data after adding a doctor
                

    
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
                self.save_data()  # Save data after updating a doctor salary


            elif user_input == '2':

                new_phone = get_valid_phone("Enter New Phone Number: ")
                doctor.phone = new_phone
                print('Doctor phone number updated successfully.')
                self.save_data()  # Save data after updating a doctor phone number


            elif user_input == '3':

                new_email = get_valid_email("Enter New Email: ")
                doctor.email = new_email
                print('Doctor email updated successfully.')
                self.save_data()  # Save data after updating a doctor email


            elif user_input == '4':

                new_name = get_non_empty_input("Enter New Name: ")
                doctor.name = new_name
                print('Doctor name updated successfully.')
                self.save_data() # Save data after updating a doctor name


            elif user_input == '5':

                new_age = get_int_input("Enter New Age: ", min_value = 1)
                doctor.age = new_age
                print('Doctor age updated successfully.')
                self.save_data() # Save data after updating a doctor age


            elif user_input == '6':

                new_department = get_non_empty_input("Enter New Department: ")
                doctor.department = new_department
                print('Doctor department updated successfully.')
                self.save_data() # Save data after updating a doctor department


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
                        self.save_data()  # Save data after deleting a doctor
                        print(f'Doctor with ID {doctor_id} deleted successfully.')
                                
                else:
                    print('Doctor deletion cancelled.')
            else:
                print('Doctor not found')

                



# ----------------------------> Employee CRUD Method ---------------------------------

# Add Employee

    def add_employee(self,employee):

        if employee.employee_id in self.employees:
            print(f'Employee with ID  {employee.employee_id} already exists')
        else:
            self.employees[employee.employee_id] = employee
            print(f'Employee {employee.employee_id} added successfully')

            self.save_data()  # Save data after adding an employee



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
                self.save_data() # Save data after updating an employee salary


            elif user_input == '2':

                new_phone = get_valid_phone("Enter New Phone Number: ")
                employee.phone = new_phone
                print("Employee Phone Number updated successfully.")
                self.save_data() # Save data after updating an employee phone number


            elif user_input == '3':

                new_email = get_valid_email("Enter New Email: ")
                employee.email = new_email
                print('Employee Email updated successfully.')
                self.save_data() # Save data after updating an employee email


            elif user_input == '4':

                new_name = get_non_empty_input("Enter New Name: ")
                employee.name = new_name
                print('Employee Name updated successfully.')
                self.save_data() # Save data after updating an employee name


            elif user_input == '5':

                new_age = get_int_input("Enter New Age: ", min_value = 1)
                employee.age = new_age
                print('Employee Age updated successfully.')
                self.save_data() # Save data after updating an employee age


            elif user_input == '6':

                new_department = get_non_empty_input("Enter New Department: ")
                employee.department = new_department
                print('Employee Department updated successfully.')
                self.save_data() # Save data after updating an employee department


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
                    self.save_data()  # Save data after deleting an employee
                    print(f'Employee {employee_id} deleted successfully.')

                else:
                    print('Employee deletion cancelled.')
            else:
                print(f'Employee {employee_id} Not Found: ')
        


# ------------------------------>  PATIENT CRUD METHOD ------------------------------


# Add Patient

    def add_patient(self,patient):

        if patient.patient_id in self.patients:
            print(f'Patient with ID {patient.patient_id} already exists.')
        else:
            self.patients[patient.patient_id] = patient
            print(f'Patient {patient.patient_id} added successfully.')

            self.save_data()  # Save data after adding a patient

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
                self.save_data() # Save data after updating a patient name


            elif user_input == '2':

                new_age = get_int_input("Enter New Age: ", min_value = 1)
                patient.age = new_age
                print("Patient Age updated successfully. ")
                self.save_data() # Save data after updating a patient age


            elif user_input == '3':

                new_phone = get_valid_phone("Enter New Phone Number: ")
                patient.phone = new_phone
                print('Patient Phone_Number updated successfully. ')
                self.save_data() # Save data after updating a patient phone number


            elif user_input == '4':

                new_email = get_valid_email("Enter New Email: ")
                patient.email = new_email
                print('Patient Email updated successfully. ')
                self.save_data() # Save data after updating a patient email


            elif user_input ==  '5':

                discharge_date = get_valid_date("Enter Discharge Date (DD-MM-YYYY): ")
                patient.discharge_date = discharge_date
                print('Patient Discharge_Date updated successfully. ')
                self.save_data() # Save data after updating a patient discharge date


            elif user_input == '6':

                new_disease = get_non_empty_input("Enter New Disease: ")
                patient.disease = new_disease
                print('Patient Disease updated successfully. ')
                self.save_data() # Save data after updating a patient disease


            elif user_input == '7':

                new_doctor_id = get_valid_doctor_id("Enter New Doctor ID: ", self.doctors)
                if new_doctor_id is not None:
                    patient.doctor_id = new_doctor_id
                    print('Patient Doctor ID updated successfully. ')
                    self.save_data() # Save data after updating a patient doctor ID
                    

            elif user_input == '8':

                new_room_number = get_available_room_number(
                    "Enter New Room Number: ",
                    self.patients,
                    current_patient_id=patient_id
                )
                patient.room_number = new_room_number
                print('Patient Room Number updated successfully. ')
                self.save_data() # Save data after updating a patient room number


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
                self.save_data() # Save data after deleting a patient
                print(f'Patient {patient_id} deleted successfully. ')

            else:
                print('Patient deletion cancelled. ')

        else:
            print(f'Patient {patient_id} Not Found: ')
