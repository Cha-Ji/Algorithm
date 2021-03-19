# Ex_1946 신입사원 [실1]
import sys
input = sys.stdin.readline
for _ in range(int(input())):   # testCase
    # input
    N = int(input())
    scoreRank = [list(map(int, input().split())) for _ in range(N)]
    scoreRank.sort()

    end = scoreRank[0][1]
    ans = 1
    for i in scoreRank:
        if i[1] < end:
            ans += 1
            end = i[1]
    print(ans)
