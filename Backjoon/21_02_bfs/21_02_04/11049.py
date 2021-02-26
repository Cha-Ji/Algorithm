# Ex_11049 행렬 곱셈 순서 [골3]
import sys
input = sys.stdin.readline
N = int(input())

mat = [list(map(int, input().split()))for _ in range(N)]

dp = [[0]*N for _ in range(N)]

for row in range(1, N):
    for col in range(N-row):
        dp[row][col] = min(
            dp[row-1][col]
            + mat[col][0] * mat[col + row][0] * mat[col + row][1],
            dp[row-1][col + 1]
            + mat[col][0] * mat[col][1] * mat[col + row][1]
        )

print(dp[row][0])
print(dp)
"""
            시작 문자
            A   B   C   D   E   F
곱셈 횟수     AB  BC  CD  DE  EF
            ABC BCD CDE DEF
            ABCD BCDE CDEF
            ABCDE BCDEF
            ABCDEF
BCD[2][1] => BC[1][1] D, B CD[1][2]
=> mat[1][0] * mat[3][0][1]
=> mat[1][0][1] * mat[3][1] 
"""
