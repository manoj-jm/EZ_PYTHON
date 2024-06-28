# s = ABABABCANFKABABCNKABABCACNDA
# P = ABABCA
#RETURN THE INDEX OF P IN S
s = "ABABABCANFKABABCNKABABCACNDA"
p = "ABABCA"
val = []
# for i in range(len(s)):
#   val.append(s[i:len(p)+i])
# print(val)

# if p in val:
#   print(val.index(p))

for i in range(len(s)):
  if s[i:len(p)+i]==p:
    print(i)
    break

# LPS ARRAY
# KMP ALGORITHM