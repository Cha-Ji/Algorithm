# Ex_10830 행렬 제곱 [골4]
# A행렬 * B행렬


def mulM(matA, matB):
    newM = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                newM[i][j] += matA[i][k] * matB[k][j]
            newM[i][j] %= 1000
    return newM


N, B = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]
result = [[1 if i == j else 0 for i in range(N)]for j in range(N)]

for i in bin(B)[2:][::-1]:
    result = mulM(result, dp) if i == '1' else result
    dp = mulM(dp, dp)

for i in result:
    print(*i)

# 1트: 10 => 5의제곱 => 4의제곱 * 1 => 2의제곱제곱 * 1 => 제곱의제곱제곱 * 1
# 2트: 10 => 5*5 => 3*2 * 3*2 => 2*1*2 * 2*1*2
# 3트: 10 => 0b1010 => 1번째 자리수부터 보면서 보텀업 방식으로 dp를 섞어 곱해나감
