# Ex_11505 구간 곱 구하기: [골1]
# 4% 시간초과 -> 펜윅트리를 만들 때부터 시간이 초과된다.
import sys
input = sys.stdin.readline

MOD = 1000000007
# 나머지 복구
def reMod(i):
    if modTree[i] > 0:
        tree[i] += MOD * modTree[i]
        modTree[i] = 0

# 나머지 처리
def mod(i):
    if tree[i] >= MOD:
        modTree[i] = tree[i] // MOD
        tree[i] %= MOD

def update(i, originNum, newNum):
    while i <= N:
        # 0으로 교체
        reMod(i)
        if originNum != 0 and newNum == 0:
            zeroTree[i] += 1
            tree[i] //= originNum

        # 0에서 교체
        elif originNum == 0 and newNum != 0:
            zeroTree[i] -= 1
            tree[i] *= newNum 

        # 일반 교체
        else:
            tree[i] //= originNum
            tree[i] *= newNum 

        mod(i)
        i += (i & -i)


def search(s, e):
    zero = 0
    ans = 1 

    # 1 ~ e 까지의 곱
    while e > 0:
        reMod(e)
        ans *= tree[e]
        zero += zeroTree[e]
        mod(e)
        e -= (e & -e)

    # 1 ~ s 까지의 곱으로 나눈다.
    while s > 0:
        reMod(s)
        ans //= tree[s]
        zero -= zeroTree[s]
        mod(s)
        s -= (s & -s)

    if zero > 0:
        return 0

    return ans % MOD

N, M, K = map(int, input().split())
tree = [1] * (N + 1)
zeroTree = [0] * (N + 1)
modTree = [0] * (N + 1)

for i in range(1, N + 1):
    update(i, 1, int(input())) # 시간초과

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(b, search(b - 1, b), c)

    elif a == 2:
        print(search(b - 1, c))                         