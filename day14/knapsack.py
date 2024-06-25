# greedy algorithm
# knapsack problem

#profit and weights
p = [5,10,15,7,8,9,4]
w = [1,3,5,4,1,3,2]

p_w = {}
#p/w 
for i in range(len(p)):
  p_w[i] = p[i]/w[i]

# print(p_w)

#sort , in list store the value in key and value format
L = list(p_w.items())
print(L)
n = len(L)

for i in range(n):
  max = i
  for j in range(i+1,n):
    if L[j][1]>L[max][1]:
      max = j
  L[i],L[max]=L[max],L[i]

print(L)

