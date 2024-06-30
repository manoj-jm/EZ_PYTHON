# find the minimum cost using greedy method , only move right and down

path = [
  [1,2,2,3],
  [3,1,4,2],
  [1,5,1,3],
  [1,2,4,1]
]
n = len(path)-1
m = len(path[0])-1
start = path[0][0]
# end = path[n-1][m-1]
i = 0
j=0
print(start)
sum=start
while i<n and j <m : 
  if path[i][j+1]< path[i+1][j]:
    j+=1
    # print(path[i][j])
    sum+=path[i][j]
  else:
    i+=1
    # print(path[i][j])
    sum+=path[i][j]

if i==n:
  while j<m:
    j+=1
    # print(path[i][j])
    sum+=path[i][j]
elif j==m:
  while i<n:
    i+=1
    # print(path[i][j])
    sum+=path[i][j]

print(sum, "value of i and j : " ,i , " ", j)