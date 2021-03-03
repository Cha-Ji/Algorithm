# Ex_10816 숫자카드 2 [실4] dict
import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
dictA = dict()

for i in a:
    if i not in dictA:
        dictA[i] = 1
    else:
        dictA[i] += 1

M = int(input())
target = list(map(int, input().split()))

for i in target:
    if i not in dictA:
        print(0, end=" ")
    else:
        print(dictA[i], end=" ")
print()
