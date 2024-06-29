def tower(n,src,dis,aux,ctr):
  if n==0:
    return
  tower(n-1,src,aux,dis,ctr)
  print(f"move {n} form {src} to {dis}")
  ctr[0]+=1
  tower(n-1,aux,dis,src,ctr)

ctr = [0]
n = 10

tower(n,'A','C','B',ctr)
print(ctr)
