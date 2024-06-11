# using recursion  , sum of the digits
n=int(input("enter the number :"))


def sumOfDigits(n):
  if n==0:
    return 0
  else:
    return n%10 + sumOfDigits(n//10)
  
res =sumOfDigits(n)
print(res)
