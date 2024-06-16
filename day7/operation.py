s = "2+2"
o = ['+','-','/','*']

x = ''
for i in s:
  if i in o:
    x = i
    s= s.replace(i," ")

l = list(map(float,s.split(" ")))
print(l)
match x:
  case '+': print(float(l[0]) + float(l[1]))
  case '-': print(float(l[0]) - float(l[1]))
  case '*': print(float(l[0]) * float(l[1]))
  case '/': print(float(l[0]) / float(l[1]))
  # case '%': float(l[0]) % float(l[1])
