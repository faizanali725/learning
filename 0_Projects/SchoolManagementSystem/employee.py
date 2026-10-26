
# ----------------------> EMPLOYEE CLASS <-------------------

class Employee:
    
    def __init__(self,employee_id:int,name:str,age:int,gender:str,job_title:str,phone_number:str,email:str,salary:float):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.gender = gender
        self.job_title = job_title
        self.phone = phone_number
        self.email = email
        self.salary = salary


    def display_info(self):
        print(f'Employee_ID:  {self.employee_id}')
        print(f'Name:  {self.name}')
        print(f'Age:  {self.age}')
        print(f'Gender:  {self.gender}')
        print(f'Job_title:  {self.job_title}')
        print(f'Phone:  {self.phone}')
        print(f'Email:  {self.email}')
        print(f'Salary:  {self.salary}')

        