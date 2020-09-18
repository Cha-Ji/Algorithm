class Solution:
    def maxProfit(self, prices) -> int:
        result = 0
        for i in range(len(prices) - 1):
            result = max(max(prices[i:]) - prices[i], result)
        return result

