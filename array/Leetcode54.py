def spiralOrder(matrix):
    result = []
        
    while matrix:
        # Add first row to result
        result.extend(matrix.pop(0))
        
        if not matrix:
            break
            
        # Rotate remaining matrix counterclockwise
        matrix = list(zip(*matrix))[::-1]
    
    return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rs = spiralOrder(matrix)
print(rs)