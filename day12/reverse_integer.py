# 94,142,104
def reverse( x: int) -> int:
        if x < 0:
            x = x * -1
        s=0
        n=x
        while n!=0:
            r = n%10
            s = s*10 + r
            n//=10
        if x < 0:
            return s*-1
        return s

print(reverse(120))
print(reverse(-321))
print(reverse(321))