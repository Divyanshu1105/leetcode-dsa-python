def maxProfit(prices):
# Treats daily price differences as an array
# Applies Kadane’s Algorithm (maximum subarray sum)
# Finds the maximum profit from one transaction

    maxCur = 0
    maxSoFar = 0

    for i in range(1, len(prices)):
        maxCur = max(0, maxCur + prices[i] - prices[i - 1])
        maxSoFar = max(maxCur, maxSoFar)

    return maxSoFar

print(maxProfit([7,1,5,3,6,4]))