from Renting import *
from sportdatabase import *

class Sports:
  def __init__(self) -> None:
    pass

  def sportEquipmentDetails(self):
    print("\nEquipment Details")
    while True:
        print("\nSport Database ")
        print("1.entryEquipment\n2.readEquipment\n3.delete(defected)\n4.update_status\n5.exit\nchoice : ")
        inpu = int(input())
        match(inpu):
          case 1:appendcontent()
          case 2:display()  
          case 3:delete()
          case 4:update_status()
          case 5 :break
          # case _ : print("invalid choice : press [cntrl + c] to exit or try-again :")
          

  def sportEquipmentRenting(self):
    while True:
      print("Renting tracking")
      print("1.barrow 2.return 3.exit")
      inpu = int(input())
      match(inpu):
        case 1:update_barrow()  
        case 2:update_return()
        case 3 : break 

  def sportEquipmentTracking(self):
    try:
      print("Sport Equipment Details")
      with open('sportequipment.txt','r') as fs:
        data = fs.read()
        # l =[str(ele) for ele in data] #to print in the form of string not in list 
        # dis = ' |'.join(l)
        print(data)

      print("\nSport Equipment Tracking")
      with open('rentaldatabase.txt','r') as f:
        data = f.readlines()
        print("usn|eid|name|time_barrowed|time_returned")
        l = [str(ele) for ele in  data]
        dis = ' |'.join(l)
        print(dis)

      
    except Exception as error :
      print(error)
    return
        
obj = Sports()

while True:
  print("Sport Equipment System")  
  ch = int(input("1.sport Equipment details\n2.sport Equipment Renting\n3.sport Equipment Tracking\n4.Exit\nenter the choice :"))
  match(ch):
    case 1: obj.sportEquipmentDetails()
    case 2: obj.sportEquipmentRenting()
    case 3: obj.sportEquipmentTracking()
    case 4: break

