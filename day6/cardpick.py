#using  sliding window technique

cards = [3,4,2,5,2,3,4,7]
window = []
inital = cards[0]
cnt = 1
for i in range(1,len(cards)):
  if inital != cards[i]:
    cnt+=1
    window.append(cards[i])
  else:
    # window.append(cards[i])
    cnt+=1
    break


print(cnt)


  
  