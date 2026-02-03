def isValid(s):
    """
    Validate if a string contains validly nested parentheses using stack.
    """
    bracket_map = {                    
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    stack = []                         
    for char in s:                      
        if char in bracket_map:        
            stack.append(char)
        elif char in ')}]':            
            if not stack:               
                return False
            opened = stack.pop()       
            if bracket_map[opened] != char:  
                return False
    
    return not stack 
    

    
s =  "([)]"
print(isValid(s))