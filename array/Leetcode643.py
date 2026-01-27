def findMaxAverage(nums ,k):
        n = len(nums)

        # sum of first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # slide the window
        for i in range(k, n):
            window_sum += nums[i]      # add right element
            window_sum -= nums[i - k]  # remove left element
            max_sum = max(max_sum, window_sum)

        return max_sum / k

