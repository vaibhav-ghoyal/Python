class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"Square is:{self.n*self.n}")

    def cube(self):
        print(f"Cube is:{self.n*self.n*self.n}")

    def squareroot(self):
        print(f"Square Root is:{self.n*1/2}")

    @staticmethod
    def greet():
        print("Hello, Good Day.!")

obj = calculator(4)
obj.greet()
obj.square()
obj.cube()
obj.squareroot()