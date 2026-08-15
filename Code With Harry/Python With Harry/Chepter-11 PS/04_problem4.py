class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self, c): # C is Call By Value OR Call By Reference ??
        return Complex(self.r +c.r,self.i+c.i)
    
    def __mul__(self, c): 
        r = self.r * c.r - self.i * c.i
        i = self.r *c.i + self.i * c.r
        return Complex(r,i)
    
    # Without Str Function Show This Error : <__main__.Complex object at 0x000001E89DBD4E10> 

    def __str__(self): 
        return f"{self.r}+{self.i}i"
    

obj1 = Complex(1,2)
obj2 = Complex(3,4)
print(obj1+obj2)
print(obj1*obj2)
        