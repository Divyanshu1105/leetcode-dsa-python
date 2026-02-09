def firstBadVersion(n):
    """
    Find the first bad version in a series using binary search.
    Notes:
    ------
    - Relies on an external `isBadVersion(version)` function that returns 
      True if the given version is bad, False otherwise
    - Uses O(log n) time complexity and O(1) space complexity
    - Implements the standard "lower bound" binary search pattern
    
    Example:
    --------
    If n = 5 and versions 3, 4, 5 are bad, returns 3
    """
    l, r = 1, n
    
    while l < r:
        mid = (l + r) // 2
        
        if isBadVersion(mid):
            r = mid  # First bad is mid or LEFT
        else:
            l = mid + 1
            
    return l
