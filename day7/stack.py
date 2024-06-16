class Stack:
  def __init__(self):
    self.plates =[]
  def push(self,ele):
    self.plates.append(ele)  
  def pop(self):
    return self.plates.pop()
  def size(self):
    return len(self.plates)
wardoor = Stack()
wardoor.push(100)
wardoor.push(500)
print(wardoor.size())