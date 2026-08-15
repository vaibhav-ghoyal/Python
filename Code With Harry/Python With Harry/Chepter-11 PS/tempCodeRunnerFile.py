def __mul__(self, c): 
        r = self.r * c.r - self.i +c.i
        i = self.r *c.i + self.i * c.r
        return Complex(r,i)