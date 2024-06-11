class Parent:
    def show(self):
        print("Parent class method")

class Child1(Parent):
    def display(self):
        print("Child1 class method")

class Child2(Parent):
    def print_message(self):
        print("Child2 class method")

# Create objects of Child1 and Child2 classes
child1 = Child1()
child2 = Child2()
child1.show()
child1.display()
child2.show()
child2.print_message()
