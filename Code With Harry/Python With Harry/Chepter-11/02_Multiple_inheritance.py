# Multiple inheritance

# Employee Parent Class
class Employee:
    company = "TCS"
    name = "Vaibhav"
    salary = 1200000

    def show(self):
        print(f"The {self.company} Name of Employee is:{self.name} And Salary is:{self.salary}")

# Another Coder Parent Class
class coder:
    language = "python"

    def printlanguage(self):
        print(f"Out of All The Language Here is Your Language:{self.language}")

# This is Child CLass Above Employee And Coder Both Parent Class Inherited in Programmer Class
class programmer(Employee,coder):
    company = "Infosys"

    def showlanguage(self):
        print(f"The Name is {self.name} And He is Good With {self.language} Language")


obj = programmer()
obj.show()
obj.printlanguage()
obj.showlanguage()