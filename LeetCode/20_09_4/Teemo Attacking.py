class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        if not timeSeries:
            return 0
        result = 0
        for i in range(0, len(timeSeries)-1):
            result += min(duration, timeSeries[i+1] - timeSeries[i])
        return result + duration
a = Solution()
print(a.findPoisonedDuration([1,2], 2))
