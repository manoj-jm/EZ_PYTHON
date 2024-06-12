import os

s = ''
with open("newFile.txt", 'r+') as f:
  data = f.readline().strip().split( ' ')
  for i in data :
    if i != 'bellary':
      # print(i,end=' ')
      if (i == '\n'):
        s+='\n'
      s+=i+' '
    else:

      l = 'bitm'
      if (i == '\n'):
        s+='\n'
      s+=l+' '
      # print(l, end=' ')

print(s)
with open('newFile.txt', 'w') as fr:
  fr.write(s)
      

  

