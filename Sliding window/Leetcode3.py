def lengthOfLongestSubstring(s):
    n = len(s)
    store = set()
    max_window = 0
    j = 0
    for i in range(n):
        while s[i] in store:
            store.remove(s[j])
            j+=1

        store.add(s[i])

        max_window = max(len(store), max_window)
    
    return max_window


s = "pwwkew"
print(lengthOfLongestSubstring(s))