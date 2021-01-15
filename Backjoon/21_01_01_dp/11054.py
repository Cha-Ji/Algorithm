#Ex_ 11054 가장 긴 바이토닉 수열
# dp로 어떻게 풀어야 할까

# s의 오름차순 부분수열
#1,5,2,1,4,3
# 1 => 1이 end인 수열 오름을 보고 추가
# 5 => 1이 end인 수열, 5가 end인 수열 보고 추가
# 2 => 1이 end인 수열, 5가 end인 수열 보고 추가
# 이전 수열 중 최댓값에서 1을 더하는 느낌
# d[0]0 = [[0],0, []]
# d[1]1 = [[1],1, []] (s[0]이 end인 수열 오름, 내림)
# d[2]5 = [[5],2, []]
# d[3]2 = [[2],2, [2],3]
# d[4]1 = [[1],1, [1],4]
# d[i] = [오름차 중인 갯수, 내림차 중인 갯수]

#수열 입력
N = int(input())
s = list(map(int, input().split()))

d = [[1,1]for _ in range(N+1)]
ans = 0
for now in range(0, N):
    # 앞선 dp 테이블을 검사
    for prev in range(0, now):
        # 오름차순 비교
        if s[now] > s[prev]:
            d[now] = [max(d[prev][0] + 1,d[now][0]),d[now][1]]
        # 내림차순 비교
        elif s[now] < s[prev]:
            d[now] = [
                d[now][0], 
                max(d[prev][0] + 1, d[prev][1] + 1, d[now][1])
                ]
                #max(오름차순 에서 전환, 내림차순 진행에 추가, 그대로) 
    ans = max(ans, d[now][1])

print(ans)





        