#find the 3 continious digits which gives you the max sum
il = [2,4,3,5,6,3,4,6,7,1,2,5]
k=int(input("enter the k "))
# maxi =0
# for i in range(len(il)-(k-1)):
#   if maxi < sum(il[i:i+k]):
#     l = il[i:i+k]
#   maxi = max(sum(il[i:i+k]),maxi)

# print(maxi,l)

#2nd approach 
'''
sum = max =0
for i in range(0,len(i)-2):
sum = l[i]+l[i+1]+l[i+2]
  if max<sum:
    max = sum
    pos = i

print(max, l[pos:i+2])
'''
# for k continious digits

max =0

for m in range(0,len(il)-k-1):
  s = 0
  s= sum(il[m:m+k])
  # for i in range(m,m+k):
    # sum+=il[i]
  if max<s:
    max = s
    pos = m

print(max, il[pos:pos+k])





  