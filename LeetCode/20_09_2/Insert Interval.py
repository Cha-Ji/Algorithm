class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()

        # 병합시키면서 버려진 배열 = [1, 0]
        # 꼬리의 숫자가 크기 때문에 비교할 때 버려진다.
        prev = intervals[0]
        rm_count = 0
        for i in range(1, len(intervals)):
            if prev[0] <= intervals[i][0] <= prev[1]:
                intervals[i] = [prev[0], max(prev[1], intervals[i][1])]
                intervals[i-1] = [1, 0]
                rm_count += 1
            prev = intervals[i]

        # 버려진 배열 제거
        for _ in range(rm_count):
            intervals.remove([1, 0])

        return intervals

a = Solution()
print(a.insert(intervals=[[0,0],[2,2],[3,3],[5,20]], newInterval=[15,17]))


