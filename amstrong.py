#import math as m
n = int(input("enter number : "))
temp = n;
m = n
sum=0
#length =int(m.log10(n)+1)
cout = 0
while n>0:
  cout=cout + 1
  n=n//10

print(cout)
while temp>0:
  rem = temp%10
  sum = sum + (rem ** cout) 
  temp=temp//10

if m == sum:
  print("Amstrong number")
else:
  print("not an Amstrong number")
