# [2,1,0,1,1,2,0,0] => [0,0,0,1,1,1,2,2] without sorting and extra list
#
# li.sort()
# print(li)
li = [2,1,0,1,1,2,0,0]
c1,c2,c0=0,0,0
for x in li:
  if x == 0:
    c0+=1
  if x == 1:
    c1 +=1
  else:
    c2 += 1

for i in range(0,len(li)):
  if i < c0:
    li[i]=0
  elif i < c0 + c1:
    li[i]=1
  else:
    li[i]=2

print(li)

  

    
