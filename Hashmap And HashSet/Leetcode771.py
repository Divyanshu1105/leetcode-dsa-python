def numJewelsInStones(jewels,stones):
    """
    Count how many of your stones are also jewels.
    
    Time Complexity: O(n + m) where n = len(stones), m = len(jewels)
    Space Complexity: O(k) where k = unique stone types in stones
    
    """
    store = {}
    count = 0
    for ch in stones:
        if ch not in store:
            store[ch] = 1
        else:
            store[ch] += 1

    for ch in jewels:
        if ch in store:
            count+=store[ch]
    
    return count



jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))