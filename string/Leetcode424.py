def characterReplacement(s,k):
    c_freq = {}
    left = 0
    max_len = 0
    for right in range(len(s)):

        if not s[right] in c_freq:
            c_freq[s[right]] = 0
        c_freq[s[right]] += 1

        count = right - left + 1
        if count - max(c_freq.values()) <= k:
            max_len = max(max_len , count)
        
        else:
            c_freq[s[left]] -= 1
            if not c_freq[s[left]]:
                c_freq.pop(s[left])
            left += 1

    return max_len



s = 'AABABBA'
k = 1
res = characterReplacement(s,k)
print(res)