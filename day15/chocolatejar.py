jar = list(map(int,input().split()))
N = int(input("no of jars ? : "))

chocolate = 0

for i in jar:
  chocolate =+i//3 
  if i%3!=0:
    chocolate +=1

print(chocolate)