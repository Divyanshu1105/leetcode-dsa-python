def isPerfectSquare(num):
    """
    Check if a number is a perfect square using binary search.
    
    Determines whether the given integer is a perfect square by searching
    for an integer whose square equals the input value.
    
    Returns:
    --------
    bool
        True if num is a perfect square, False otherwise
        
    Notes:
    ------
    - Uses binary search for O(log n) time complexity
    - Handles the edge case where num = 1 (which is a perfect square)
    - Only searches up to num//2 since sqrt(num) ≤ num//2 for num > 1
    """
    l = 0
    r = num//2
    if num == 1:
        return True
    while l<=r:
        mid = (l+r)//2
        res = mid * mid
        if res == num:
            return True 
        elif res < num:
            l = mid + 1
        else: 
            r = mid - 1
    return False

num = 16
print(isPerfectSquare(num))