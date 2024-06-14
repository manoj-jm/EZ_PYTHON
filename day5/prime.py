def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
number = int(input("enter num :"))
result = is_prime(number)
print(f"The number {number} is {'a prime number' if result else 'not a prime number'}.")





# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# # Example usage
# number = int(input("enter the number : "))
# result = is_prime(number)
# print(f"The number {number} is {'a prime number' if result else 'not a prime number'}.")
