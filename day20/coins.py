# what will be the min no of coins required to pay the bill
# greedy method
bill_amt = int(input("Enter the bill amount: "))
c = 0
coins = [7, 5, 1]  # Largest to smallest coin values

for coin in coins:
    if bill_amt == 0:
        break
    if bill_amt >= coin:
        count = bill_amt // coin  
        c += count
        bill_amt -= count * coin  

print("Minimum number of coins needed:", c)
