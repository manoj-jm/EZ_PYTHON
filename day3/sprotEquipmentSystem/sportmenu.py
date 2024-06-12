import os
import datetime as dt

class Sports:
  def __init__(self) -> None:
    self.eid = 0
  def sportEquipmentDetails(self):
    print("Equipment Details")
    print("1.entry\n2.read")
    def entry():
      with open('sportequipment.txt','wb') as fw : 
        self.eid = input("enter equipment id : ")
        ename = input("enter equipment name : ")
        econdition = input("enter equipment condition : ")
        estatus = input("enter equipment id : ")
        d = f'{self.eid},{ename},{econdition},{estatus}'
        fw.write(d.encode())

    def read():
      with open('sprotequipment.txt','r') as fr:
        fr.read();
        

    while True : 
      sch = int(input("enter choice : "))
      match(sch):
        case 1: entry()
        case 2: read()

  def sportEquipmentRenting(self):
    print("Equipment Renting")
    print("1.barrow\n2.return")
    def barrow():
      with open('studentequipment.txt','w') as fw : 
        sname = input("enter equipment sname : ")
        usn = input("enter equipment usn : ")
        eid = self.eid # check here ? 
        time_barrow = dt.datetime()
        time_retrn = ''
        d = f'{sname},{usn},{eid},{time_barrow},{time_retrn}'
        fw.write(d.encode())

    def retrn():
      usn = int(input("enter the usn of the student : "))
      
      with open('sprotequipment.txt','r') as fr:
       
        

         while True : 
          sch = int(input("enter choice : "))
          match(sch):
            case 1: barrow()
            case 2: retrn()


obj = Sports()
while True:
  ch = int(input("enter the choice : 1.sport Equipment details\n2.sport Equipment Renting\n3.sport Equipment Tracking"))
  match(ch):
    case 1: obj.sportEquipmentDetails()
    case 2: obj.sportEquipmentRenting()
    case 3: obj.sportEquipmentTracking()
    case _: break
