# pattern1
print("pattern 1")

for i in range(0,4):
  print('*'*4)

#pattern2
print("pattern 2")
for i in range(0,4+1):
  print("*"*i)

#pattern3
print("pattern 3")

for i in range(1,4+1):
  for j in range(1,i+1):
    print(j,end=" ")
  print("")

#pattern4
print("pattern 4")

for i in range(1,4+1):
  for j in range(1,i+1):
    print(i,end=' ')
  print('')

#pattern5
print("pattern 5")
for i in range(5,0,-1):
  print("*"*i)

#pattern6
print("pattern 6")
for i in range(5,0,-1):
  for j in range(1,i+1):
    print(j,end='')
  print('')


# #pattern7
print("pattern 7")

n=5
for i in range(n+1):
  print(" " * (n-i) + "*" * (2*i -1))

#patter8
print("pattern 8")
n=5
print('pattern 8 ')
for i in range(n,0,-1):
  print(" " * (n-i) + "*" * (2*i -1))


# daimond 9
print("pattern 9")
for i in range(n):
  print(" " * (n-i) + "*" * (2*i -1))
for i in range(n,0,-1):
  print(" " * (n-i) + "*" * (2*i -1))
  

#pattern 10
print("pattern 10")
for i in range(n):
  print("*"*i)
for i in range(n,0,-1):
  print("*"*i)


#pattern11
print("pattern 11")
m = 1
for i in range(1,6):
  for j in range(1,i+1):  
    if (i+j)%2 == 0:
      print(1 , end='')
    else:
      print(0 , end='')
  print('')

  

#pattern12
print("pattern 12" , end='\n')
n=4
space = 2 * (n -1)
# print(space)
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end='')

  for k in range(space,0,-6):
    print(" " * k ,end='')

  for j in range(i,0,-1):
    print(j,end='')
  print('')
  space-=2

#pattern 13
print("pattern 13")
start = 1
n = 5
for i in range(n+1):
  for j in range(i):
    print(start,end=' ')
    start+=1
  print('')


#pattern 14
print("pattern 14")
n = 5
for i in range(1,n+1):
  char = 65
  for j in range(char,char+i):
    print(chr(char), end=' ')  
    char+=1
  print()

print("pattern 15")
#pattern 15
n = 5 
print("\n")
for i in range(n,0,-1):
  ch = 65
  for j in range(i):
    print(chr(ch),end=' ')
    ch+=1
  print('')

#pattern 16
print("pattern 16")
n = 5
c = 65 
for i in range(1,n+1):
  for j in range(i):
    print(chr(c),end=' ')
  c+=1
  print('')


# pattern 17
print("pattern 17")
n = 5

for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end=' ')
  cp = 65
  for j in range(i):
    print(chr(cp),end=' ')
    cp+=1
  cp = cp - 2 # 2 letters backwords 
  for j in range(i-1):
    print(chr(cp),end=' ')
    cp-=1
  print('')

'''
You are given a number N and you have to print the given pattern:
For N=3
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1
'''
N = 3
n = 3
# for i in range(n):
#   for j in range(n,i,-1):
#     for k in range(n):
#       print(j,end=' ')
#     print('')


#pattern 18
# n = 6
# revchr = 70
# for i in range(n):
#   for j in range(i):
#     print(chr(revchr),end=' ')
#     revchr+=1
#   revchr-=1
#   print('')

print("pattern 18 a \n")
n = 6
revchr = 70
for i in range(n):
  rev = revchr
  for j in range(i):
    print(chr(rev),end=' ')
    rev+=1
  revchr-=1

  print('')



#pattern 18
print("pattern 18 b\n")
n=4
space = 2 * (n -1)

N=4
spc =0
for i in range(N,0,-1):
  for j in range(i):
    print("*",end='')
  
  for m in range(0,spc):
    print(" ",end='')
  
  for j in range(i):
    print("*",end='')
  print("")
  spc += 2
#second thrown
for i in range(1,n+1):
  for j in range(1,i+1):
    print("*",end='')

  for k in range(space,0,-6):
    print(" " * k ,end='')

  for j in range(i,0,-1):
    print("*",end='')
  print('')
  space-=2



#pattern 20
print("pattern 20")
n=4
space = 2 * (n -1)
N=4
spc =0
for i in range(1,n+1):
  for j in range(1,i+1):
    print("*",end='')

  for k in range(space,0,-6):
    print(" " * k ,end='')

  for j in range(i,0,-1):
    print("*",end='')
  print('')
  space-=2
#second 
for i in range(N,0,-1):
  for j in range(i):
    print("*",end='')
  
  for m in range(0,spc):
    print(" ",end='')
  
  for j in range(i):
    print("*",end='')
  print("")
  spc += 2


#pattern 21
print("pattern 21")
num = 5
for i in range(num):
  for j in range(num):
    if j==0 or i==0 or i==num-1 or j == num-1 :
      print("*",end=' ')
    else:
      print(" ",end=' ')
  print('')


#pattern 21
print("pattern 21 \n")
n = 4
for i in range(2*n):
  for j in range(2*n - 1):
    top , left , bottom , right = i , j ,(2*n -2)-i,(2*n -2)-j
    res = min(min(top,bottom),min(left,right))
    print(n-res,end=' ')

  print('')



