#power of two numbers using recursion

def powerOfNumber(base,expo):
  if expo == 0:
    return 1
  else:
    return base * powerOfNumber(base,expo-1)
  
print(powerOfNumber(2,3))
