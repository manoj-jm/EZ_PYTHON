# There is no overloading(compile time p) in polymorphism
#constructor polymorphism , latest will consider . 
#in python , only operator overloading is posible , not for function and constructor polymorphis

# run time polymorphism (overriding), same function name , but implementation , functionality is differnce
# function and constructor overriding is possible in python.
class c1:
  def __init__(self) -> None:
    print("parent class")
  def add(self):
    print(10 + 30)


class c2(c1):
  def __init__(self) -> None:
    print("child class")
  def add(self):  #overriding the add in c1
    print(10*20)

obj = c2()
obj.add()