# Parent Class
class Employee:
    company = "ITC"

    def show(self):
        print(f"The Name of Employee is {self.name} And The Salary is {self.salary}")

# class Programmer:
#     company = "ITC"
#     def show(self):
#         print(f"The Name of Employee is {self.name} And The Salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The Name is {self.name} And He is Good With {self.language} Language")

# Child Class
class programmer(Employee):
    company = "ITC Infotech"

    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary

    def showlanguage(self):
        print(f"The Name is {self.name} And He is Good With {self.language} Language")


obj1 = Employee()

obj2 = programmer("Vaibhav","Python",120000)
obj2.show()
obj2.showlanguage()
print(obj1.company,"\n",obj2.company)