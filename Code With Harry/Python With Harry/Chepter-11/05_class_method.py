# Class Method - it Used To Access Class Attribute Value Rathen then Attribute Value.

class Employee:
    ename = "Vaibhav"

    # Class Method is Used to Access Attribute of Class Value.
    @classmethod 
    def show(cls):
        print(f"The Class Attribute of Employee Name is {cls.ename}")


e = Employee()
e.ename = "Shiv"

e.show()