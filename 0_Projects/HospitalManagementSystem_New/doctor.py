# ---------------- Doctor Class -----------------

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

