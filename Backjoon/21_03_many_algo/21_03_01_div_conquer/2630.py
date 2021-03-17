# Ex_2630 색종이 만들기 [실3]
def sol(x, y, w, ans):
    if w * w * board[x][y] == sum(sum(board[x + i][y: y + w]) for i in range(w)):
        ans[board[x][y]] += 1

    else:
        w //= 2
        for dx, dy in (0, 0), (0, w), (w, 0), (w, w):
            ans = sol(x + dx, y + dy, w, ans)
    return ans


N = int(input())
board = [list(map(int, input().split()))for _ in range(N)]
ans = sol(0, 0, N, [0, 0])
print(ans[0])
print(ans[1])
