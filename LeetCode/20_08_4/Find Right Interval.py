class Solution:
    def findRightInterval(self, intervals):
        resultList = [-1] * len(intervals)

        # start point는 중복되지 않으므로
        # dict형의 인덱스로 사용
        dictInput = {}
        dictIndex = 0
        for i in intervals:
            dictInput[i[0]] = dictIndex
            dictIndex += 1

        sortedInput = sorted(intervals)

        # right interval이 될 수 있는 가장 가까운 요소를 찾는다.
        for i in range(len(sortedInput) - 1):
            for j in range(i + 1, len(sortedInput)):
                # 배열의 몇 번째 요소의 right_interval이 몇 번째 요소인지 찾는다.
                if sortedInput[j][0] >= sortedInput[i][1]:
                    index = dictInput[sortedInput[i][0]]
                    result = dictInput[sortedInput[j][0]]
                    resultList[index] = result
                    break

        return resultList

a = Solution()
print(a.findRightInterval([[1,4],[2,3],[3,4]]))
