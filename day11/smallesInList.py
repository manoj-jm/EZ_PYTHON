li = [13,1,42,9,28,0,-3,-1] # find the smallest positive integer
li.sort()
print(li)
# [-2,-1,0,1,2,4,3]
for i in li:
  if i>0:
    print(i)
    break    
  
# leetcode 41
result = 1
for i in li:
  if result == i:
    result+=1

print(result)
