from collections import defaultdict

def minWindow(s,t):
    if len(s) < len(t):
        return ""
    char_count = defaultdict(int)
    for ch in t:
        char_count[ch] += 1

    min_window = (0, float("inf"))
    start_index = 0
    target_count_remain = len(t)

    for end_index, ch in enumerate(s):
        if char_count[ch] > 0:
            target_count_remain -= 1
        char_count[ch] -= 1

        if target_count_remain == 0:
            while True:
                char_at_start = s[start_index]
                if char_count[char_at_start] == 0:
                    break
                char_count[char_at_start] += 1
                start_index += 1
            
            if end_index - start_index < min_window[1] - min_window[0]:
                min_window = (start_index , end_index)

            
            #adjust for validity
            char_count[s[start_index]] += 1
            target_count_remain += 1
            start_index += 1

    return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1] 

s = "ADOBECODEBANC"
t = "ABC"
result = minWindow(s,t)
print(result)