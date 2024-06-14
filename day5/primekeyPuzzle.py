'''
Problem Statement: 
In the enchanted land of Numeria, Alice is on a quest to find the legendary 
Prime Key to unlock the ancient Vault of Secrets. The vault's guardian, an 
ancient sphinx, presents a multi-step puzzle that Alice must solve to obtain the 
Prime Key. 
The puzzle consists of multiple levels, each requiring Alice to solve a different 
challenge involving prime numbers. To progress through each level, Alice must 
perform the following tasks: 
Level 1: Find the smallest  number larger than a given integer N. 
Level 2: Calculate the sum of all prime numbers between N and the smallest 
prime number larger than  N. 
Level 3: Determine if the product of the smallest prime number larger than N 
and the next immediate prime number is also a prime. 

To complete the puzzle and retrieve the Prime Key, Alice must solve these 
challenges in sequence for a given integer N. 

Your task is to write a function that takes an integer N and returns a tuple 
containing the following: - The smallest prime number larger than N (Level 1 result). - The sum of all prime numbers between N and the smallest prime number 
larger than N (Level 2 result). - A boolean indicating whether the product of the smallest prime number 
larger than N and the next immediate prime number is prime (Level 3 result). 
Help Alice navigate through the levels, solve the puzzle, and obtain the Prime 
Key to unlock the Vault of Secrets.'''

def isprime(n):
    flag =0
    if n <= 1:
        flag = 1
    elif n==1:
       flag =0
    else: 
      for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
              flag = 1
              break
          
      if flag ==0:
         return 1
      else:
         return 0
  
    
N = int(input("enter the number : "))

t = []

flag =0
k = N + 1
while flag<1:
  flag = isprime(k)
  if flag == 1:
    t.append(k)
  else:
    k+=1
print(k)

sum =0
for i in range(N+1,k):
   sum+=i

t.append(sum)

p1 =k 
flag =0
k=p1+1
while flag<1:
  flag = isprime(k)
  if flag == 1:
    p2 = k
  else:
    k+=1

print(p2)
p3 = p1 * p2

boolvalue = True if isprime(p3)== 1 else False
t.append(boolvalue)
tup = tuple(t)
print(tup)
      


  