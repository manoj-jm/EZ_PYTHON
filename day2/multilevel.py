class Grandparent:
    def show(self):
        print("Grandparent class method")

class Parent(Grandparent):
    def display(self):
        print("Parent class method")

class Child(Parent):
    def print_message(self):
        print("Child class method")

# Create an object of the Child class
child = Child()
child.show()
child.display()
child.print_message()
