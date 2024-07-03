inp_list = list(map(int,input().split()))
k = int(input())

li = [0]*k
for i in inp_list:
  li[i-1]+=1

print(li)



