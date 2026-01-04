def FindLargeThree(arr):
    newA =  sorted([arr[0],arr[1],arr[2]])
    for idx in range(3,len(arr)-1):
        sorter = len(newA)-1
        value = arr[idx]
        while 0 < sorter:
            target = newA[sorter]
            if newA[sorter] < value: 
                newA[sorter] = value
            sorter -=1
    return newA

arr = [34,1,-32,-1,35,2,78,90,45,123,-3,32]
print(FindLargeThree(arr))