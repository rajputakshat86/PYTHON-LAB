class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):
        print("This is Child class method (Overriding Parent method)")

p = Parent()
p.show()

c = Child()
c.show()