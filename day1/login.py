#write a program to build login system using funcitons .  the function name should be login and register 
# 1 . ask user to enter the details for registration  and   out of all its details only user name and passwrod should be stored
# 2  . now this funciton should ask user to enter user name and password and check whether if these match with the register details , lgoin successfull otherwise repeat this login process , saying invalid credentials.

database = {}
def register():
  print("-----------registeration----------")
  name=input("enter the username : ")
  pas=input("enter the password : ")
  # gen = input("enter the Gender : ")
  # age=input("enter the age : ")
  # roll=input("enter the rollNo : ")
  database[name] = pas 
  print("registeration done ")
    
def login():
  while True:
    print("---------login------------")
    username = input("Username : ")
    password = input("Password : ")
    if username in database:
      if password == database[username]:
        print("Login success ")
        break
      else : 
        print("invalid password ")
        pass
    else:
      print("user not found ! , register first")
        

while True:
  ch = int(input("enter the choice : 1.register , 2.login , 3.exit "))
  match(ch):
    case 1:register()
    case 2:login()
    case 3:break
    

