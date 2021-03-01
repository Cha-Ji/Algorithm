# Ex_11049 행렬 곱셈 순서 [골3]
N = int(input())
mat = [list(map(int, input().split()))for _ in range(N)]
dp = [[0]*N for _ in range(N)]

# count = 문자 갯수, start = 시작 문자 번호
for count in range(1, N):
    for start in range(N-count):
        # 목표 행렬을 두 행렬묶음의 곱이라고 생각하고
        # 앞 행렬, 뒤 행렬, 자르는 중간 지점을 갖고 계산한다.

        # 재사용할 변수 = 첫[0] * 끝[1]
        mulTemp = mat[start][0] * mat[start + count][1]

        # 초기화 = 첫 번째 값
        minScore = dp[0][start] + \
            dp[count-1][start+1] + mulTemp * mat[start][1]

        for mid in range(start + 1, count + start):
            # dp[문자 개수][시작 문자]
            # 행렬묶음의 문자 개수
            frontCount = mid - start
            endCount = count - frontCount - 1

            # 각 행렬 묶음의 dp값 dp[문자개수][시작문자]
            frontDp = dp[frontCount][start]
            endDp = dp[endCount][mid + 1]
            mulMat = mulTemp * mat[mid][1]

            minScore = min(minScore, frontDp + endDp + mulMat)

        dp[count][start] = minScore

print(dp[count][0])

"""
            시작 문자
곱셈 횟수     A       B       C       D       E       F
1           AB      BC      CD      DE      EF
2           ABC     BCD     CDE     DEF
3           ABCD    BCDE    CDEF
4           ABCDE   BCDEF
5           ABCDEF

ABCDE[0][4] = A * BCDE, AB * CDE, ABC * DE, ABCD * E
A * BCDE = [0][0] + [3][1]  +  A[0] * E[1] *A[1]
AB * CDE = [1][0] + [2][1]  +  A[0] * E[1] *B[1]
ABC * DE = [2][0] + [1][1]  +  A[0] * E[1] *C[1]
            앞     + 뒤      +  temp        *mid+start[1]  

"""
