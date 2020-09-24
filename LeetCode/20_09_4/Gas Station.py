class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        length, max_profit = len(gas), [0, 0]
        for index in range(length):

            profit = gas[index]
            for now in range(index, index + length):
                now %= length
                next = (now + 1) % length
                profit = profit + gas[next] - cost[now]
                if profit <= 0:
                    break
            profit -= cost[index]

            if profit > max_profit[0]:
                max_profit = [profit, index]

        return max_profit[1]

a = Solution()
print(a.canCompleteCircuit([4,5,2,6,5,3],
[3,2,7,3,2,9]))

