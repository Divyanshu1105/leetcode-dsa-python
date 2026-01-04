"""
Problem: Valid Palindrome II
Approach:
- Use two pointers
- On first mismatch, try skipping either side
- Check remaining substring

Time: O(n)
Space: O(1)
"""


def validPalindrome(s):
    def is_pal(l, r):
            while l < r:
                    if s[l] != s[r]:
                        return False
                    l += 1
                    r -= 1
                    return True            

            first, last = 0, len(s) - 1

            while first < last:
                if s[first] == s[last]:
                    first += 1
                    last -= 1
                else:
                    # try skipping either side
                    return is_pal(first + 1, last) or is_pal(first, last - 1)

            return True

print(False or True)