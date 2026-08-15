# Super Keyword :- Super Keyword is Reference Variable Create Instance of Parent Class Access Method,Constructor,Attribute(Variable)

class Employee:
    def __init__(self):
        print("Employee Class Constructor.")

class Manager(Employee):
    def __init__(self):
        print("Manager Class Constructor.")
        super().__init__() # Super Keyword point to Parent Class Constructor

class Programmer(Manager):
    def __init__(self):
        print("Programmer Class Constructor.")
        super().__init__() # Super Keyword point to Parent Class Constructor


obj = Programmer()
