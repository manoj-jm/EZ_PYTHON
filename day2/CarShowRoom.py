# create a class carshowroom in which  
# - create a func named carcompany which will allow user to select a car company out of displayed companies if the user enter any random car campany , he/she asked to re-enter .
# -according to the carcompany selected the user should be re-directed to selecting the models of  that company out of the given list .if anything other model enter , ask for re-enter 
# -after selecting the model the user should re-directed to selecting the varient(petrol / diesel ).
# -according to the car campany model and varient a price should be calculated to which SGST & CGST are added to make it the total price . NOTE : SGST and CGST are common for all the  cars

carcampany = ["BMW" , "Mercedes"]
carmodels = { 1 : "1.BMW-M4 \n2.BMW-M5" , 2:"1.M-300c \n2.M-60Z"}
carmodelprice = { 1:{1:5400 , 2:9100 }, 2: { 1:8900 , 2: 9000} }
varient = ['petrol', 'diesel'];

#price = self.carmodprice[ch][mch]


class carShowRoom:
  
  def __init__(self,carcampany,carmodels,carmodelprice) -> None:
    print("Welcome")
    print("carshowroom :\n1.BMW \n2.Mercedes")
    self.carcompany = carcampany
    self.carmodels = carmodels
    self.carmodprice = carmodelprice
   

  def carCompany(self):
    self.varient = varient
    while True:
      print('car companies : ' ,self.carcompany)
      self.ch = int(input("enter the carcampany : ")) 
      if self.carcompany[self.ch-1] in self.carcompany :
        self.carModel(self.ch)
        break
      if self.ch > 2:
        print("wrong choice , re-enter : ")


  def carModel(self,ch):
      print(f"car campany selected {self.carcompany[ch-1]}")
      print("MODELS")
      print(self.carmodels[ch])
      while True:
        mch = int(input("enter model : "))
        if mch == 1:  
          vch = input("enter the varient : petrol/diesel : ")
          if vch == 'petrol':
            sgst = 2.09
            cgst =2.09
            price =0
            price = self.carmodprice[ch][mch]
            sgst = 2.09 *price
            cgst = 2.09 *price
            tot = sgst + cgst + price
            print(f"total price is {tot}")
            return
          if vch == 'diesel':
            sgst = 2.1
            cgst =2.1
            price =0
            price = self.carmodprice[ch][mch]
            sgst = 2.09 * price
            cgst = 2.09 * price
            tot = sgst + cgst + price
            print(f"total price is {tot}")
            return;

        if mch == 2:
            vch = input("enter the varient : petrol/diesel : ")
            if vch == 'petrol':
              sgst = 2.09
              cgst =2.09
              price =0
              price = self.carmodprice[ch][mch]
              sgst = 2.09 *price
              cgst = 2.09 *price
              tot = sgst + cgst + price
              print(f"total price is {tot}")
              return;
            if vch == 'diesel':
              sgst = 2.1
              cgst =2.1
              price =0
              price = self.carmodprice[ch][mch]
              sgst = 2.09 * price
              cgst = 2.09 * price
              tot = sgst + cgst + price
              print(f"total price is {tot}")
              return;   
        else:
          print("re-enter : ")


cust1 = carShowRoom(carcampany,carmodels,carmodelprice)
cust1.carCompany()





