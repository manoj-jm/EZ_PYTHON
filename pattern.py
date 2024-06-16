for i in range(0,4):
  print('*'*4)

#pattern2
for i in range(0,4+1):
  print("*"*i)

#pattern3
for i in range(1,4+1):
  for j in range(1,i+1):
    print(j,end=" ")
  print("")

#pattern4
for i in range(1,4+1):
  for j in range(1,i+1):
    print(i,end=' ')
  print('')

#pattern5
for i in range(5,0,-1):
  print("*"*i)

#pattern6
for i in range(5,0,-1):
  for j in range(1,i+1):
    print(j,end='')
  print('')


# #pattern7
# for i in range(1,6):
#   for j in range(i*5-1):
#     print("*" * j, end='')
#   for j in range(i):
#     print("*"*i,end='')
#   print('')


    