class Employee:
    empid = 101

    @classmethod
    def show(cls):
        print(f"The Class Attribute Of a is {cls.empid}")

    @property
    def ename(self):
        return f"First Name is:{self.fname}\nLast Name is:{self.lname}"
    
    @ename.setter
    def ename(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


obj = Employee()

obj.empid=105

obj.ename = "Vaibhav Ghoyal"
print(f"First Name is:{obj.fname}\nLast Name is:{obj.lname}")

obj.show()