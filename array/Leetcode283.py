def moveZeroes(arr):
    # SOl -1
        #  o(n2) - time complexity
        # for i in range(len(arr)-1):
        #     if arr[i] != 0:
        #         continue
        #     for j in range(i+1, len(arr)):
        #         if arr[j] != 0:
        #             arr[i] = arr[j]
        #             arr[j] = 0
        #             break


        # sol-2  
        # O(n) - time and in-place
        pos = 0  # position for next non-zero

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1

print(moveZeroes([0,1,1,0]))