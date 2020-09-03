class Solution:
    def firstStock(self, prices, i):
        profit = 0
        buyPrice = prices[0]
        sellPrice = 0
        # j라는 기준점을 두고,
        # 왼쪽 그룹의 최솟값을 buyPrice
        # 오른쪽 그룹의 최댓값을 sellPrice로 한다.
        for j in range(0, i+1):
            try:
                buyPrice = min(prices[:j])
            except:
                buyPrice = prices[0]
            try:
                sellPrice = max(prices[j+1:i])
            except:
                sellPrice = prices[i]
            profit = max(profit, sellPrice - buyPrice)
        return profit

    def secondStock(self, prices, i):
        profit = 0
        buyPrice = prices[i]
        sellPrice = 0

        for j in range(i, len(prices)+1):
            try:
                buyPrice = min(prices[i:j])
            except:
                buyPrice = prices[i]
            try:
                sellPrice = max(prices[j+1:])
            except:
                sellPrice = prices[-1]
            profit = max(profit, sellPrice - buyPrice)
        return profit
    def maxProfit(self, prices) -> int:
        # i라는 기준점을 두고, prices[:i], prices[i+1:] 두 개의 그룹으로 나눈다.
        # 각 그룹에서 최적의 거래를 찾는다.
        profit = 0
        for i in range(0, len(prices) - 1):
            profit = max(profit, self.firstStock(prices, i) + self.secondStock(prices, i))
            print(self.firstStock(prices,i),self.secondStock(prices,i))
        return profit

a = Solution()
print(a.maxProfit([2,1,4,5,2,9,7]))
