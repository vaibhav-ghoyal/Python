class Employee:
    name="Vaibhav"
    language="Python"
    salary=120000

    # Constructor
    def __init__(self,name,language,salary): # It is Dunder Method Which is Automatically Called.
        #self.name = name
        #self.language = language
        #self.salary = salary
        print(f"Employee Name is:{name}\nEmployee languge is:{language}\nEmployee Salary:{salary}")
        print("I Am Creating An Object Constructor Automatically Call.")

    # Simple Member Function or Simple Method
    def getinfo(self):
        print(f"Employee Name is:{self.name}\nEmployee Language is:{self.language}\nEmployee Salary is:{self.salary}")

    # Static Method
    @staticmethod
    def greet():
        print("Hello,Vaibhav Mahadev.")


obj = Employee("Vaibhav","JavaScript",130000)
obj.getinfo() # Employee.getinfo(obj)
obj.greet()
