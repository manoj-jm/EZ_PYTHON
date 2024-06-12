import os

with open("practicefile.txt", 'wb')as fs:
  eid = input("enter the equipment id : ")
  name = input("enter name : ")
  usn = input("enter usn : ")
  s = f"{eid},{name},{usn}"
  fs.write(s.encode())

  