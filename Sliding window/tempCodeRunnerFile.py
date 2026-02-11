def characterReplacement(s,k):
    counts = [0] * 26
    start = 0
    maxCharCount = 0
    result = 0

    for end in range(len(s)):
        idx = ord(s[end]) - ord('A')
        counts[idx] += 1

        # only increase
        maxCharCount = max(maxCharCount, counts[idx])

        # shrink if invalid
        while (end - start + 1) - maxCharCount > k:
            counts[ord(s[start]) - ord('A')] -= 1
            start += 1

        result = max(result, end - start + 1)

    return result

s = "AABABBA", k = 1
print(characterReplacement(s,k))