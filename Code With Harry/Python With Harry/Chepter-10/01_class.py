# Create Class With Datamember(Variable or Attribute)

# Class Creation
class Employee:
    name="Vaibhav"
    language = "Python"
    salary = 120000

# Object Creation
obj = Employee()
obj.age = 20

# Display Detail of Employee Class
print("Employee Name is:",obj.name) # print(f"Employee Name is:{obj.name}") Modern Way Using Format String
print("Employee Age is:",obj.age)
print("Employee Language is:",obj.language)
print("Employee Salary is:",obj.salary)