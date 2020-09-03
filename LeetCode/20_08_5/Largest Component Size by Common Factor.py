from math import gcd

class Solution:
    def largestComponentSize(self, A) -> int:
        # component size를 탐색
        def search(graph, index, size):
            while graph[index] != 0:
                size += 1
                index = graph[index]
            return size

        #graph와 유사한 배열
        graphList = [0]*100001

        # i,j가 이어짐을 graphList[i] = j로 표현
        # graph[i] 값이 없으면 끊어짐,
        # 값이 있으면 그 값과 그래프가 이어짐
        for i in A:
            for j in A:
                if i == j:
                    continue
                if gcd(i, j) != 1:
                    graphList[i] = j

        maxSize = 0
        for i in range(len(A)-1):
            maxSize = max(maxSize, search(graphList, A[i], 0))

        return maxSize

a = Solution()
print(a.largestComponentSize([4,6,15,35]))
