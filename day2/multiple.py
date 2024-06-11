class Parent1:
    def show(self):
        print("Parent1 class method")

class Parent2:
    def display(self):
        print("Parent2 class method")

class Child(Parent1, Parent2):
    def print_message(self):
        print("Child class method")

# Create an object of the Child class
child = Child()
child.show()
child.display()
child.print_message()
