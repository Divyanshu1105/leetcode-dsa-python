def countBit(n):       
    # ans = []
    # count = 0 
    
    # while count <= n:
    #     ones = 0
    #     value = count
    #     while value!=0:
    #         ones += (value&1)
    #         value >>=1
    #     ans.append(ones)
    #     count += 1
    # return ans

    ans = [0] * (n+1)
    for i in range(1,n+1):
        ans[i] = ans[i>>1] + (i&1)
    return ans

print(countBit(123))