# Ex_1620 나는야 포켓몬 마스터 이다솜 [실4]
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mon = {}

for i in range(1, N + 1):
    name = input()[:-1]
    mon[name] = i
    mon[str(i)] = name

for _ in range(M):
    print(mon[input()[:-1]])
