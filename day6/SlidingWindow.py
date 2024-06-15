il = [2,4,3,5,6,3,4,6,7,1,2,5]

window = max = 0
k = int(input("enter the no of continious digit : "))

for  j in range(0,k):
  window+=il[j]

for i in range(0,len(il)-k):
  if max<window:
    max = window
    pos = i
  window = window - il[i] + il[i+k]

print(max , il[pos:pos+k])