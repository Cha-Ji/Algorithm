#Ex_ 1700 멀티탭 스케줄링 [골드2]
import sys
import heapq
N, K = map(int, input().split())
S = list(map(int, sys.stdin.readline().split()))

# elec[제품번호] = [대기표]
# 대기표가 먼 제품 먼저 뽑는다.
elec = [[101]for i in range(K+1)]
for i in range(K-1, -1, -1):
    elec[S[i]].append(i+1)

# 전자제품 꽂기
ans = 0
hole = [-1] * (N+1)
sinkHole = 0 # 빈 구멍 인덱스
thisHole = 0
delHole = [] # [-대기표, 구멍 번호]

for i in range(K):
    thisElec = elec[S[i]].pop() #대기표 접수
    nextElec = elec[S[i]][-1]   #대기표 확인

    if S[i] not in hole:
        # 빈 구멍 있는지 확인
        if sinkHole < N:
            hole[sinkHole] = S[i]
            thisHole = sinkHole
            sinkHole += 1
            
        # 뽑기
        else:
            ans += 1
            trash, thisHole = heapq.heappop(delHole)
            hole[thisHole] = S[i]
    # 꽂혀있으면 어디 꽂혔는지
    else:
        for j in range(N):
            if hole[j] == S[i]:
                thisHole = j

    heapq.heappush(delHole, [-nextElec, thisHole])

print(ans)




