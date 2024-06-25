p = [5,10,15,7,8,9,4]
w = [1,3,5,4,1,3,2]

n = len(p)
c = 15

def cal_max(P,W,C,n):
        for i in range(n+1):
            for j in range(C+1):
                if j - W[i-1]<0:
                    dp[i][j]=dp[i-1][j]
                else: 
                  dp[i][j]=max(dp[i-1][j],p[i-1]+dp[i-1][j-w[i-1]])

                  
dp=[[0 for i in range(c+1)] for j in range(n+1)]
    
print(cal_max(p,w,c,n))
print(dp)
