from Renting import *
from sportdatabase import *

class Sports:
  def __init__(self) -> None:
    pass

  def sportEquipmentDetails(self):
    print("\nEquipment Details")
    while True:
        print("Sport Database ")
        print("1.entryEquipment\n2.readEquipment\n3.delete(defected)\n4.update_status\nchoice : ")
        inpu = int(input())
        match(inpu):
          case 1:appendcontent()
          case 2:display()  
          case 3:delete()
          case 4:update_status()
          case _ :break
          # case _ : print("invalid choice : press [cntrl + c] to exit or try-again :")
          

  def sportEquipmentRenting(self):
    while True:
      print("Renting tracking")
      print("1.barrow 2.return")
      inpu = int(input())
      match(inpu):
        case 3:update_barrow()  
        case 4:update_return()
        case _ : break 

  def sportEquipmentTracking():
    display()
    return
        
obj = Sports()

while True:
  print("Sport Equipment System")  
  ch = int(input("1.sport Equipment details\n2.sport Equipment Renting\n3.sport Equipment Tracking\nenter the choice :"))
  match(ch):
    case 1: obj.sportEquipmentDetails()
    case 2: obj.sportEquipmentRenting()
    case 3: obj.sportEquipmentTracking()
    case _: break

