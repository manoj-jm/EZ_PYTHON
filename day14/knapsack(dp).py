# job_profit = { 'j1':20,'j2':40,'j3':10,'j4':30,'j5':50}
# job_deadline = {'j1':2,'j2':1,'j3':2,'j4':3,'j5':1}


def calc_max(p,w,c,n):
  if n==0 or c == 0:
    return 0
  if (w[n-1]>c):
    return calc_max(p,w,c,n-1)
  else:
    return max(p[n-1]+calc_max(p,w,c-w[n-1],n-1),calc_max(p,w,c,n-1))

# p = [5,10,15,7,8,9,4]
# w = [1,3,5,4,1,3,2]
# c = 15
# n = len(p)
# val = calc_max(p,w,c,n)
# print(val)

#using memonization ie: recursion + data storing
p = [5,10,15,7,8,9,4]
w = [1,3,5,4,1,3,2]
c = 15
n = len(p)
DP = [[-1 for i in range(c+1)] for j in range(n+1)]
val = calc_max(p,w,c,n)
print(val)
