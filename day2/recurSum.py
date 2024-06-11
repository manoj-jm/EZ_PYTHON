n=7645 # using recursion  , sum of the digits


def sumOfDigits(n):
  if n==0:
    return 0
  else:
    i = n%10
    n = n//10
    return i + sumOfDigits(n)
  
res =sumOfDigits(n)
print(res)
