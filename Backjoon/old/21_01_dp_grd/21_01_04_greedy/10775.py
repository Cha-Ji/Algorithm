# Ex_10775 공항 [골드1]
import sys
import heapq

G = int(input())
P = int(input())

# g[walk]칸으로 가시오.
g = [-1] * (G+1)

for i in range(P):
    walk = int(sys.stdin.readline())
    # 빈자리 도킹
    if g[walk] == -1:
        g[walk] = walk - 1  # 다음칸

    # 앞에 도킹
    else:
        thisWalk = g[walk]  # g[walk] 칸으로 가시오
        # 빈자리 찾아가기
        while thisWalk > 0:
            if g[thisWalk] == -1:
                g[thisWalk] = thisWalk - 1  # 다음 칸
                g[walk] = thisWalk - 1
                break
            thisWalk = g[thisWalk]

        # 도킹 실패?
        if thisWalk == 0:
            i -= 1
            for _ in range(P-i-1):
                sys.stdin.readline()
            break

print(i + 1)
