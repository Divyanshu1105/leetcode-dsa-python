def lengthOfLongestSubstring(s):
    # store = set()
    left = 0
    maxLen = 0

    """Using HashSet"""
    # for right in range(len(s)):
    #     if s[right] not in store:
    #         store.add(s[right])
    #         maxLen = max(maxLen , right - left + 1)
    #     else:
    #         while s[right] in store:
    #             store.remove(s[left])
    #             left += 1 
    #         store.add(s[right])
    # return maxLen


    store = {}
    """Using HashMap"""
    for right in range(len(s)):
        if s[right] not in store or store[s[right]] < left:
            store[s[right]] = right
            maxLen = max(maxLen , right - left + 1)
        else:
            left = store[s[right]] + 1
            store[s[right]] = right
    
    return maxLen

str = "pwwwwwwkew"
res = lengthOfLongestSubstring(str)
print(res)