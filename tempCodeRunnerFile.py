n=3
for i in range(n):
        for j in range(n, i, -1):
            print((str(j) + " ") * (n-i), end="")
        print()