
# ---------------- Patient Class ------------------------

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
