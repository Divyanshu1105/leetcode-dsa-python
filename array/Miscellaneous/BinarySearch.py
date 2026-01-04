def BinaryS(arr,target):
    low = 0
    high = len(arr)-1
    while low < high:
        med = (low + high)//2
        if arr[med] == target:
            return med
        elif arr[med] < target: 
            low += 1
        else:
            high -= 1
    return -1


arr = [0, 11,22,45,67,89,123,476,789,999,2111]
print(BinaryS(arr,788))