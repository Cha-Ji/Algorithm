class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        start_road = trips[0][1]
        end_road = trips[-1][2]
        road = [0] * 1001

        for i in trips:
            for j in range(i[1], i[2]):
                road[j] += i[0]
        print(road)
        return max(road) <= capacity
a = Solution()
print(a.carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3))


