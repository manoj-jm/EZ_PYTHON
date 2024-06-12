import os

with open("newFile.txt", 'r+b') as f:
  print(f.tell())
  f.seek(-32,2)# 2 is the 3rd line last character
  print(f.tell())
  f.write(b"bitm   ")
  print(f.read().decode('utf-8'))
  f.close()
  


  

