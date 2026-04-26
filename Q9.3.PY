class Parent:
    def show_parent(self):
        print("Parent Class")

class Child1(Parent):
    def show_child1(self):
        print("Child1 Class")

class Child2(Parent):
    def show_child2(self):
        print("Child2 Class")

class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(B):
    def show_c(self):
        print("Class C")

class M1:
    def show_m1(self):
        print("Class M1")

class M2:
    def show_m2(self):
        print("Class M2")

class Multiple(M1, M2):
    def show_multiple(self):
        print("Multiple Inheritance Class")

class Hybrid(B, Child1):
    def show_hybrid(self):
        print("Hybrid Inheritance Class")


print("Single Inheritance")
c = Child1()
c.show_parent()
c.show_child1()

print("\nHierarchical Inheritance")
c1 = Child1()
c2 = Child2()
c1.show_parent()
c1.show_child1()
c2.show_parent()
c2.show_child2()

print("\nMultilevel Inheritance")
obj = C()
obj.show_a()
obj.show_b()
obj.show_c()

print("\nMultiple Inheritance")
m = Multiple()
m.show_m1()
m.show_m2()
m.show_multiple()

print("\nHybrid Inheritance")
h = Hybrid()
h.show_a()
h.show_b()
h.show_child1()
h.show_hybrid()