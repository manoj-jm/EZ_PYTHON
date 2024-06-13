marks = {}

class Student:
  def __init__(self,name,usn,marks) -> None:
    self.name = name
    self.usn = usn
    self.marks = marks
    self.Mark = []
    marks[self.usn] = self.Mark
    self.percentage = None
    self.grade = None

  def updateMarks(self):
    # m1 = int(input("enter the marks of sub1 : "))
    # m2 = int(input("enter the marks of sub2 : "))
    # m3 = int(input("enter the marks of sub3 : "))
    # m4 = int(input("enter the marks of sub4 : "))
    # m5 = int(input("enter the marks of sub5 : "))
    # self.Mark.insert(0,m1)
    # self.Mark.insert(1,m2)
    # self.Mark.insert(2,m3)
    # self.Mark.insert(3,m4)
    # self.Mark.insert(4,m5)
    for i in range(0,5):
      m4 = int(input(f"enter the marks of sub{i+1} : "))
      self.Mark.insert(i,m4)
    
    
    # marks[self.usn] = self.Mark
    
  def display(self):
    print(f"Name\t\t|USN\t|s1  |s2  |s3  |s4  |s5 |Percentage |Grade |")
    # print(self.name , end='\t\t|')
    # print(self.usn , end='\t|')
    l = [str(ele) for ele in  self.marks[self.usn]]
    dis = '  |'.join(l)
    print(f"{self.name}\t\t|{self.usn}\t|{dis} |{self.percentage}\t|{self.grade}\t|")
    if self.Mark == []:
      # print('\t | \t|\t |\t |\t |',end=' ')
      print(f"{self.name}\t\t|{self.usn}\t|  |  |  |  |  |{self.percentage}\t|{self.grade}\t|")

    # print(dis , end=' |')
    # self.percent()
    # print(self.percentage,end=' |')
    # print(self.grade,end=' |')

  def percent(self):
    self.percentage = (sum(self.Mark) / 500 )*100
    if self.percentage <=100 and self.percentage >81:
      self.grade = 'A'
    if self.percentage <=80 and self.percentage >61:
      self.grade = 'B'
    if self.percentage <=60 and self.percentage >36:
      self.grade = 'C'
    elif self.percentage>0 and self.percentage<=35:
      self.grade = 'F'
    return self.percentage
  

    



while True:
  ch = int(input("\n1.student_admission 2.update_marks 3.display_record : "))
  match(ch):
    case 1:
      name = input(f'\nenter student name : ')
      usn = input('enter student usn : ')
      s = Student(name,usn,marks)
    case 2:
      s.updateMarks()
    case 3:
      s.display()
    
      
      
    



  
    
    