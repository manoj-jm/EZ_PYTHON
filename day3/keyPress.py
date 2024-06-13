'''vote_list = list(map(int,input("enter the votes ").split(" ")))
# they are 6 candidates .
count = [0]*6
for i in vote_list:
  count[i-1]+=1

max_votes = max(count)
print(max_votes)'''

target = int(input("enter the numeric string s :"))
keyboard = [0,1,2,3,4,5,6,7,8,9,00]
cnt = 0
display = 0
flag = 0
print("value is : ", display)
while True:
  k = int(input("enter the number : "))
  if k in keyboard:
    if k == 00 :
      display = display * 100
      cnt+=1
      if display > target:
        flag=0
        break
      if display == target:
        flag = 1
        break
    else:
      display = (display * 10) + k
      print(" value is : " , display ,"and ", target)
      cnt+=1
      if display > target:
        flag=0
        break
      if display == target:
        # print(" value is : " , display ,"and ", target)
        # print("no of count : ", cnt)
        flag = 1
        break
  else:
    print(f"not in keyboard {keyboard}!")

if flag == 1:
  print(f"Number of steps to reach to target {target} : {cnt} " )
else:
  print(f"Not matching steps to reach target { target} ")
        


      





