class twoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def display(self):
        print(f"The Vector is {self.i}i + {self.j}j")

class threeDvector(twoDvector): # twoDvector class inherited 
    def __init__(self,i,j,k): 
        super().__init__(i,j) # Calling a Parent Class Constructor Using Super Keyword
        self.k = k

    def show(self): 
        super().display() # Calling a Parent Class Method using Super Keyword
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")


obj = threeDvector(2,3,4)

obj.show()