class Animals:
    pass

class pets(Animals):
    pass

class dog(pets):

    @staticmethod
    def bark():
        print("Bhow Bhow..!")


obj = dog()
obj.bark()