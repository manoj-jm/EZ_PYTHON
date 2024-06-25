# greedy algorithm
# knapsack problem
import math as m
#profit and weights
p = [5,10,15,7,8,9,4]
w = [1,3,5,4,1,3,2]

# capacity = int(input("enter the max capacity of knapsack : "))

p_w = {}
#p/w 
for i in range(len(p)):
  p_w[i] = p[i]/w[i]


# print(p_w)

#sort , in list store the value in key and value format
L = list(p_w.items())
print(L)
n = len(L)
# approach 1  using lamda function
L.sort(key=lambda x:x[1],reverse=True)
print(L)

# for i in range(n):
#   max = i
#   for j in range(i+1,n):
#     if L[j][1]>L[max][1]:
#       max = j
#   L[i],L[max]=L[max],L[i]
# print(L)


#current weight 
# curr_w = 0
# for i in range(len(L)):
#   if curr_w < weight : 
#     curr_w += L[i][1]
  
# print(m.ceil(curr_w))