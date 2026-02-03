def isAnagram(s,t):
        # store = {}


        # if len(s) != len(t):
        #     return False

        # for ch in t:
        #     if ch not in store:
        #         store[ch] = 1
        #     else:
        #         store[ch] +=1 

        # for ch in s:
        #     if ch in store and store[ch] > 0:
        #         store[ch] -= 1
        #     else:
        #         return False
        
        # return True
        
        """
    Check if two strings are anagrams using array counter.
    
    Args:
        s, t: Strings containing lowercase English letters.
    
    Returns:
        True if s and t are anagrams, False otherwise.
    
    Time: O(n), Space: O(1) - uses fixed array of 26."""
    

        if len(s) != len(t):
            return False

        # Initialize counter array for 26 lowercase letters
        char_count = [0] * 26

        # Count characters in s
        for ch in s:
            char_count[ord(ch) - ord('a')] += 1

        # Subtract characters from t
        for ch in t:
            index = ord(ch) - ord('a')
            char_count[index] -= 1
            # Early exit if count goes negative
            if char_count[index] < 0:
                return False

        # Verify all counts are zero (redundant with early exit, but safe)
        return all(count == 0 for count in char_count)

s="ab"
t="aa"
print(isAnagram(s,t))