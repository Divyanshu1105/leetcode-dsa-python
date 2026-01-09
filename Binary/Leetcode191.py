def hammingWeight(n):

    """ approach 1 """
    # rem = ''
    # while n > 0:
    #     rem = str(n%2) + rem
    #     n = n // 2
    
    # count = 0 
    # for i in rem:
    #     if i == '1':
    #         count += 1
    
    # return count

    """ approach 2 """
    """
        
    """
    ones = 0
    while n!=0:
        ones = ones + (n&1)
        n = n >> 1
    return ones

n = 2147483645
res = hammingWeight(n)
print(res)