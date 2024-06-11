# given : 2, 4,2,0,21,0,48 , output : 2,4,2,21,48 ,0, 0
#no extra list is used (constraints)
#no 2 for loops used
#no swap , use two pointer approach

# approach 1:
# arr = [4,0,5,0,1,9,0,0] 
# for x in range(0,len(arr)):
#   if arr[x]==0:
#     temp = arr.pop(x)
#     arr.insert(len(arr)-1 , temp)
# print(arr)


arr = [4,0,5,0,1,9,0,0]
j = 0
for i in range(0,len(arr)):
  if arr[i]!=0:
    arr[j]=arr[i]
    j+=1

while j<len(arr):
  arr[j]=0
  j+=1

print(arr)


    

    

 



