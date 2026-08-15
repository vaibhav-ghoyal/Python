class Vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
    # def __add__(self, a):
    #     result = Vector(self.x + a.x , self.y + a.y , self.z + a.z)
    #     return result
    
    # def __mul__(self, m):
    #     result = self.x * m.x + self.y * m.y + self.z * m.z
    #     return result
    
    # def __str__(self):
    #     return f"Vector({self.x},{self.y},{self.z})"
    
    
# Test The Implementation
obj1 = Vector([1,2,3])
print(len(obj1))