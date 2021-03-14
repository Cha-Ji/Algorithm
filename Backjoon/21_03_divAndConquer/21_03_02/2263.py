# Ex_2263 트리의 순회 [골3]
import sys
sys.setrecursionlimit(10**6)

n = int(input())
# 양 쪽 서브트리를 알아낼 수 있다.
inOrder = list(map(int, input().split()))
# 맨 뒤에 루트가 있다.
postOrder = list(map(int, input().split()))

inOrderDict = [0] * (n + 1)
for i in range(n):
    inOrderDict[inOrder[i]] = i


def preOrder(sIn, eIn, sPost, ePost):
    if sIn > eIn or sPost > ePost:
        return

    # 후위 순회는 마지막에 루트노드가 온다.
    root = postOrder[ePost]
    # 중위 순회에서 루트 노드를 기점으로 좌우 트리를 나눈다.
    mid = inOrderDict[root]

    # 중위 순회에서 나눈 결과를 토대로 갯수를 맞춘다.
    leftNodeCount = mid - sIn
    midPost = sPost + leftNodeCount

    print(root, end=" ")
    preOrder(sIn, mid - 1, sPost, sPost + leftNodeCount - 1)
    preOrder(mid + 1, eIn, sPost + leftNodeCount, ePost - 1)


preOrder(0, n-1, 0, n-1)
print()
