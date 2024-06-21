#find the number of commas between 1 and 1 lakh
n = 12349920
if n< 1000:
  print("zero commas")
else:
  count = (len(str(n))-1)//3 
  print(count)

#count = str(n).count(',')