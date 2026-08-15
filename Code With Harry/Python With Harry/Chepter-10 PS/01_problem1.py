class programmer:
    company = "Microsoft"
    def __init__(self,name,language,salary,pin):
        self.name = name
        self.language = language
        self.salary = salary
        self.pin = pin


obj1 = programmer("Vaibhav","Python",120000,364004)
print(f"Programmer name is:{obj1.name}\nProgrammer salary is:{obj1.salary}\nProgrammer pincode is:{obj1.pin}")
print("\n")
obj2 = programmer("Shiv","Block Chain",130000,364004)
print(f"Programmer name is:{obj2.name}\nProgrammer salary is:{obj2.salary}\nProgrammer pincode is:{obj2.pin}")