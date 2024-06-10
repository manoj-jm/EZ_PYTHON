#power is done , by power to position of digit
#problem is , muiltiple the digit and its current position 
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
  p = rem ** cout
  sum = sum + p
  cout -=1 
  temp=temp//10

print(sum)