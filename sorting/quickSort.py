def partition(arr , low , high):
    pivot = arr[high]

    i = low - 1

    for j in range(low,high):
        if pivot > arr[j]:
            i += 1
            swap(arr , i , j)

    
    swap(arr , i+1 , high)
    return i + 1

def swap(arr , i ,j):
    arr[i] , arr[j] = arr[j] , arr[i]


def quickSort(arr, low , high):
    if low > high:
        return arr
    pi = partition(arr , low , high)
    quickSort(arr, low , pi - 1)
    return quickSort(arr , pi + 1 , high)



arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

print(quickSort(arr, 0 , n-1))
