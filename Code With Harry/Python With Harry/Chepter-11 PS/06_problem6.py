class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, a):
        result = Vector(self.x + a.x , self.y + a.y , self.z + a.z)
        return result
    
    def __mul__(self, m):
        result = self.x * m.x + self.y * m.y + self.z * m.z
        return result
    
    def __str__(self):
        return f"{self.x}i+{self.y}j+{self.z}K"
    
# Test The Implementation
obj1 = Vector(1,2,3)
obj2 = Vector(4,5,6)
obj3 = Vector(7,8,9) # Same Dimesion Vector

print(obj1 + obj2) # output : Vector(5, 7, 9)
print(obj1 * obj2)

print(obj1 + obj3)
print(obj1 * obj3)