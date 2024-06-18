list = [12,42,13,82,9,28,49]
n = len(list)
for i in range(1,n):
  x =  list[i]
  j = i -1
  while j >= 0 and list[j] > x:
    list[j+1] = list[j]
    j-=1
  list[j+1] = x
  
print(list)
          