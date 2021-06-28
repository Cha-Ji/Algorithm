# Ex_9375 패션왕 신혜빈: [실3]
import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    wear = defaultdict(int)
    for _ in range(int(input())):
        wear[input().split()[1]] += 1

    ans = 1
    for key in wear.keys():
        ans *= wear[key] + 1

    print(ans - 1 if wear else 0)
