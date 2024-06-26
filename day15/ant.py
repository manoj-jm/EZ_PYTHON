# problem is to find and "return" how many times the ant reachs back to its original starting position
N = int(input(" what is the number "))
# arr = input().split()
# map(datatype, list)
arr = list(map(int,input().split()))
cnt =0
print(arr)
for i in range(1,len(arr)):
  if sum(arr[:i+1])== 0:
    cnt+=1
print(cnt) 