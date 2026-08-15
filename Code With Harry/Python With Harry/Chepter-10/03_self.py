class Employee:
    name = "Vaibhav"
    language = "Python"
    salary = 120000

    # Simple Member Function or Simple Method
    def getdata(self):
        print(f"Employee Name is:{self.name}\nEmployee Language is:{self.language}\nEmployee Salary is:{self.salary}")

    # Static Method
    @staticmethod
    def greet():
        print("Good Morning")


obj = Employee() # Object Creation
obj.getdata() #Employee.getdata(obj)
obj.greet()