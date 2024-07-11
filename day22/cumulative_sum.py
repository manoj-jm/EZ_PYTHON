arr = [ -1 , 4 , 7 , 2]

# cumulative sum of an arr
carr = []
s = 0
for i in range(0,len(arr)):
  s = sum(arr[:i+1])
  carr.append(s)

print(carr)