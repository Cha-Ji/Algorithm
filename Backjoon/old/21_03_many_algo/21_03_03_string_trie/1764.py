# Ex_1764 듣보잡 [실4]
import heapq
N, M = map(int, input().split())
noHear = set(input() for _ in range(N))

noNamed = []
for _ in range(M):
    noSee = input()
    if noSee in noHear:
        heapq.heappush(noNamed, noSee)

print(len(noNamed))

while noNamed:
    print(heapq.heappop(noNamed))
