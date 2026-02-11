def characterReplacement(s,k):
    """
    LeetCode 424 — Longest Repeating Character Replacement

    Sliding Window + Frequency Count

    We maintain a window [start, end] and track character frequencies
    inside it using a fixed-size array (26 for uppercase letters).
    maxCharCount stores the highest frequency of any single character
    seen in the current window (updated only when expanding).

    Key Idea:
    To make all characters in the window identical, we must replace
    (window_size - maxCharCount) characters. The window is valid if
    this value is <= k.

    Time Complexity: O(n)
    Space Complexity: O(1) — fixed 26-size frequency array
    """
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

s = "AABABBA"
k = 1
print(characterReplacement(s,k))