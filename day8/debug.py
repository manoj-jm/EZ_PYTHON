def isPalindrome( x: int) -> bool:
      if str(x)==str(x)[::-1]:
            return True
      return False
        

print(isPalindrome(383))