op = {}
ip = [[2,2,1,2,1],[4,2,3,1,2,1,2,3],[1,1,1,1,1],[3,0,3],[1,2,1,1,2,1],[1,1,1,2,1],[5,2,1,3,1,2,5]]

def isequal(subip):
  for i in subip:
    mid = len(subip)//2
    lhs = sum(subip[:i])
    rhs = sum(subip[i:])
    if lhs==rhs:
      mid=i
  
  return mid

j=1
for i in ip:
  res = isequal(i)
  k = f'checkpoint{j}'
  j+=1
  op[k]=res

print(op)

