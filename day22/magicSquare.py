inp = [
  [4,3,8],
  [9,5,1],
  [2,7,6]
]

row_sum = []

for i in range(len(inp)):
  row_sum.append(sum(inp[i]))
# print(row_sum)

dia_sum =[]
ds =0
rds=0
for i in range(len(inp)):
  for j in range(len(inp)):
    if i == j : 
      ds += inp[i][j]

for i in range(len(inp)):
  for j in range(len(inp),-1,-1):
    if i == j:
      rds +=inp[i][j]

dia_sum.append(ds)
dia_sum.append(rds)
# print(dia_sum)

# column sum 
tc = 0
fc = 0
sc =0
cs = []
for i in range(len(inp)):
  for j in range(len(inp)):
    if i == 0:
      fc += inp[i][j]
    if i == 1:
      sc += inp[i][j]
    if i == 2:
      tc +=inp[i][j]

cs.append(fc)
cs.append(sc)
cs.append(tc)

# print(cs)
arr = list(tuple(row_sum) + tuple(cs)+tuple(dia_sum))
print(arr)

flag = True
for i in range(len(arr)-1):
  if arr[i]!=arr[i+1]:
    flag = False


    

if flag==True:
  print("It is Magic square")
else:
  print("It is not a Magic square")






  

  
    
    
    

