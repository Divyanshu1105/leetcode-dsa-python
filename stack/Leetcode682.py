def calPoints(operations):
    """
        Implements a stack-based solution to process operations on a counter value using O(1) space.
    Returns:
        int: Final sum of all valid counter values after processing operations
        
    
    Time: O(n), Space: O(n)
    Stack maintains history of valid operations for D/+ operations.
    """
    res = []
    for i in range(len(operations)):
        if operations[i] == 'C':
            res.pop()
        elif operations[i] == "D":
            val = res[-1] * 2
            res.append(val)
        elif operations[i] == "+":
            val = res[-1] + res[-2]
            res.append(val)
        else:
            res.append(int(operations[i]))
    
    return sum(res)

ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))