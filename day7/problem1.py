#check wether the expression given by that boy is valid or not 
class Stack:
  def __init__(self):
    self.plates =[]
  def push(self,ele):
    self.plates.append(ele)  
  def pop(self):
    return self.plates.pop()
  def size(self):
    return len(self.plates)
  def disp(self):
    print(self.plates)
  def top(self):
    if len(self.plates)==0:
      return 0
    return self.plates[-1]

check_exp = Stack()

samp_in = "{[3+7{52/11(3+5)}]}[]"
open= '{[('
close = ')]}'
for i in samp_in:
  if i in open:
    check_exp.push(i)
    # open+=1
  if i == ']' and check_exp.top() == '[':
    check_exp.pop()
  elif i==')' and check_exp.top() == '(':
    check_exp.pop()
  elif i=='}' and check_exp.top() == '{':
    check_exp.pop()
  elif i in close:
    check_exp.push(i)
print(check_exp.size())

if check_exp.size() == 0:
  print("valid expression")
else:
  print("Invalid expression")

'''
optimal solution 



'''
  

