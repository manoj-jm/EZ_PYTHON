#lps:00012
#ABCABCABC
#000123456 # matching count of letters
# finding the pattern using kmp O(n+m)

def KMPAlgo(p,s):
  M = len(p)
  N = len(s)
  lps = []
  LPS(p,M,lps)
  print(lps)
  i=0
  j=0
  while (N-i)>=(M-j):
    if p[j]==s[i]:
      i+=1
      j+=1

    if j == M:
      print("patern found ", i-j)
      j = lps[j-1]
    elif i<N and p[j]!=s[i]:
      if j!=0:
        j = lps[j-1]
      else:
        i+=1
   




   








if __name__ == "__main__":
  s = "ABABABCABCABCABFKABABCNKABABCACNDA"
  p = "ABCAB"
  KMPAlgo(p,s)

