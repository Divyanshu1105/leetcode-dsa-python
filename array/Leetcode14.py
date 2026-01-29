def longestCommonPrefix(strs):
    if not strs:
            return ""
    
    if len(strs) == 1:
        return strs[0]
    
    # Take first string as reference
    for i in range(len(strs[0])):
        char = strs[0][i]
        
        # Check this character with all other strings
        for j in range(1, len(strs)):
            # If other string is shorter or character doesn't match
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]  # Return prefix up to mismatch
    
    return strs[0]

strs = ["flower","flow","flight"]

res = longestCommonPrefix(strs)
print(res)