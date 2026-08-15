# Multilevel Inheritance 

class one:
    one = "One-Parent Class"

    def show(self):
        print(self.one)

class two(one):
    two = "two-Another inherited Class"

    def display(self):
        print(self.two)

class three(two):
    three = "three-Child Class"

    def showdata(self):
        print(self.three)


t = three()
t.show()
t.display()
t.showdata()