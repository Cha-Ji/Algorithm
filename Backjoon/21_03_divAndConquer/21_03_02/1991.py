# Ex_1991 트리 순회 [실1]
import sys
input = sys.stdin.readline


def order(root):
    if root in tree:
        ans[0] += root
        order(tree[root][0])
        ans[1] += root
        order(tree[root][1])
        ans[2] += root


tree = dict()
ans = [""] * 3
for _ in range(int(input())):
    root, l, r = map(str, input().split())
    tree[root] = [l, r]
order("A")
print("\n".join(ans))
