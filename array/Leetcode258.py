def addDigits(num):
        currSum = 0
        numStr = str(num)
        i = 0
        while len(numStr) != 1:
            if i < len(numStr):
                currSum += int(numStr[i])
                i+=1
            else:
                numStr = str(currSum)
                currSum = 0
                i = 0

        return int(numStr)

print(addDigits(12349))
