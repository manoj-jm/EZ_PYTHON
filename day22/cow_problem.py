def is_safe(stalls, k, min_dist):
    count = 1  # Place the first cow in the first stall
    last_position = stalls[0]
    
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]
            if count == k:
                return True
    return False

def aggressive_cows(stalls, k):
    stalls.sort()
    low = 1  # Minimum possible distance
    high = stalls[-1] - stalls[0]  # Maximum possible distance
    best = 0
    
    while low <= high:
        mid = (low + high) // 2
        if is_safe(stalls, k, mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return best

# Example usage
stalls = [1, 2, 4, 8, 9]
k = 3
print(aggressive_cows(stalls, k)) 
