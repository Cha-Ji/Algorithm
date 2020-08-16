class Solution:
    def min(self,a,b): return a if a < b else b
    def max(self,a,b): return b if a < b else a

    def maxProfit(self, prices) -> int:
        if len(prices) == 1: return 0

        # first buy
        firstBuy = prices[0]
        for i in range(len(prices)):
            if prices[i] < prices[i+1]:
                firstBuy = min(firstBuy, prices[i])


