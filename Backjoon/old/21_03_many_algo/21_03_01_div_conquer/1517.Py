# Ex_1517 버블소트 [골1]
def addNode(node, s, e, num):
    if s <= num <= e:
        tree[node] += 1
        if s < e:
            addNode(node * 2, s, (s + e) // 2, num)
            addNode(node * 2 + 1, (s + e) // 2 + 1, e, num)

    elif num < s:
        ans[0] += tree[node]


n = int(input())
A = list(map(int, input().split()))
dictA = dict().fromkeys(sorted(A), 0)

# 1 7 9 4 2 => 1 4 5 3 2
for index, key in enumerate(dictA):
    dictA[key] = index + 1

for old in range(n):
    A[old] = dictA[A[old]]

#
tree = [0] * 4 * n
ans = [0]
for num in A:
    addNode(1, 0, n-1, num - 1)
print(*ans)
"""
tree[node] = 인덱스는 작은데 크기는 큰 수의 갯수
이전에 들어온 수 중 나보다 큰 수

"""
