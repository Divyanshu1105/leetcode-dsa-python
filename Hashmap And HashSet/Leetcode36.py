def isValidSudoku(board):
        store= {}
        for val in range(0,len(board),3):
            l = val
            k = val + 1
            m = val + 2
            count = 0
            fill_validation = 0
            j = 0 
            while j < len(board[0]):
                if board[l][j] not in store:
                    store[board[l][j]] = True
                else:
                    if board[l][j] == ".":
                        fill_validation += 1
                    else: 
                        return False
                
                if board[k][j] not in store:
                    store[board[k][j]] = True
                else: 
                    if board[k][j] == ".":
                        fill_validation += 1
                    else:
                        return False
                
                if board[m][j] not in store:
                    store[board[m][j]] = True
                else: 
                    if board[m][j] == ".":
                        fill_validation += 1
                    else:
                        return False
                
                j+=1
                count +=1 
                if count == 3:
                    if fill_validation == 9:
                        return False
                    store = {}
                    count = 0
                    fill_validation = 0
        
        return True



board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(board))