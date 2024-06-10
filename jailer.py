n = int(input("enter the no_prisoner :"))
c = int(input("enter the no_chacolate :"))
s = int(input("enter the start_prisoner :"))
 
# c = 10 , n=6  , s = 3 
# output = 6
# c_distribution =       3 4 5 6 7 8 9 10 11 12 
# no_prisoner_circular = 3 4 5 6 1 2 3  4  5  6 

last_prisoner = ((s+c) -1) % n
if last_prisoner == 0:
  print(n)
else:
  print(last_prisoner)
