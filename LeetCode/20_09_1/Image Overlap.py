class Solution:
    def largestOverlap(self, A, B) -> int:
        # 겹친 1을 구하는 함수
        def overlap(A, B, n) -> int:
            result = 0
            i = n[0] if n[0] > 0 else 0
            while i - n[0] < length and i < length:
                j = n[1] if n[1] > 0 else 0
                while j - n[1] < length and j < length:

                    # and 연산으로 비교
                    if (A[i - n[0]][j - n[1]] and B[i][j]) == 1:
                        result += 1
                    j += 1
                i += 1
            return result

        # 전체 평면을 상하좌우로 움직이는 함수
        def bfs():
            stack = list([i, j]for i in range(-length+1, length)for j in range(-length+1, length))
            largest = overlap(A, B, [0, 0])

            while stack:
                n = stack.pop()
                if promissing(n[0], n[1], largest):
                    largest = max(overlap(A, B, n), largest)
            return largest

        # 최댓값에 도달할 수 없을 경우 false
        def promissing(x, y, largest) -> bool:return (length - x)*(length - y) >= largest

        length = len(A)

        return bfs()

print(Solution.largestOverlap(Solution, A=[[1, 0], [0, 0]], B=[[0, 1], [1, 0]]))
print(Solution.largestOverlap(Solution, A = [[1,1,0],
            [0,1,0],
            [0,1,0]],
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]))
