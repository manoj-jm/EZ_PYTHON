class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def display(self):
        print("Child class method")

# Create an object of the Child class
child = Child()
child.show()
child.display()
