
# --------------------> Teacher Class <--------------------------

class Teacher:

    def __init__(self,teacher_id:int,name:str,age:int,gender:str,subject:str,phone_number:str,email:str,salary:int):
        self.teacher_id = teacher_id
        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject
        self.phone_number = phone_number
        self.email = email 
        self.salary = salary



    def display_info(self):
        print(f" Teacher ID:  {self.teacher_id}")
        print(f" Name: {self.name}")
        print(f" Age: {self.age}")
        print(f" Gender: {self.gender}")
        print(f" Subject {self.subject}")
        print(f" Phone Number: {self.phone_number}")
        print(f" Email: {self.email}")
        print(f" Salary: {self.salary}")




    