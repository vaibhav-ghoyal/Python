class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self, no):
        return self.n + no.n
    
    def __sub__(self, no):
        return self.n - no.n
    
    def __mul__(self, no):
        return self.n * no.n
    
    def __truediv__(self, no):
        return self.n / no.n
    
    

n = Number(4)

m = Number(5)

print(n+m)