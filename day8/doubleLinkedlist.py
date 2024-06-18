#double lined lis

class Node:
    def __init__(self, value):
        self.value = value
        self.Left = None
        self.Right = None

class List:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

        
    def insert_front(self, val):
        new_node = Node(val)
        if self.head == None:
          self.head = new_node
          self.count+=1
        else:
           new_node.Right = self.head
           self.head.Left = new_node
           self.head = new_node
           self.count+=1
           
    def insert_end(self,val):
        new_node = Node(val)
        if self.head==None:
          self.head = new_node
          self.count+=1
        else:
          curr = self.head
          while curr.Right:
            curr = curr.Right
          curr.Right = new_node 
          new_node.Left = curr
          self.count+=1

    
    def insert_mid(self,val,pos):
        new_node = Node(val)
        if self.head==None:
          self.head = new_node
          self.count+=1

        else:
            count = 1
            curr = self.head
            while count < pos:
              prev = curr
              count+=1
              curr = curr.Right
            new_node.Right = curr
            curr.Left = new_node
            prev.Right = new_node
            new_node.Left = prev
            self.count+=1

    def display(self):
       if self.head == None:
          print("list is empty ")
       else:
          curr = self.head
          while curr:
            print(curr.value,end='\n')
            curr = curr.Right


    def delete_front(self):
        if self.head ==None:
          print("list is empty ")
        else:
          curr = self.head
          self.head = curr.Right
          self.head.Left = None
          curr.Right = None

    def delete_end(self):
        if self.head == None:
          print("list is empty ")
        else:
            curr = self.head
            while curr.Right:
              p = curr
              curr  =curr.Right
            print(curr.value)
            curr.Left = None
            p.Right = None

    def delete_mid(self,pos):
        if self.head == None:
          print("list is empty ")
        else:
           c =1
           curr = self.head
           while c<pos:
              p = curr
              c+=1
              curr = curr.Right
           p.Right = curr.Right
           curr.Right = None
           curr.Left = None
            
          

            
l = List()

while True:
   
    ch = int(input("1.insert_front 2.insert_end 3.insert_mid 4.delete_front 5.delete_end 6.delete_mid 7.display : "))

    match(ch):
      case 1:
          ele = int(input("enter the data  : "))
          l.insert_front(ele)
      case 2:
          ele = int(input("enter the data : "))
          l.insert_end(ele)
      case 3:
          ele = int(input("enter the data : "))
          pos = int(input("enter the position : "))
          l.insert_mid(ele,pos)
      case 4:l.delete_front()    
      case 5:l.delete_end()   
      case 6:
          pos = int(input("enter the position : "))      
          l.delete_mid(pos) 
      case 7:l.display()
      case _:break