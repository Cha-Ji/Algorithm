# Ex_1987 알파벳 [골4]

def stoi(s):
    return ord(s) - ord('A')


def isPromising(x, y):
    # 좌표의 범위
    if 0 <= x < R and 0 <= y < C:
        # 방문했으면 False
        return not visited[stoi(board[x][y])]
    return False


def dfs(x, y, depth):
    ans[0] = max(ans[0], depth)
    # 종료 조건
    if ans[0] == stoi('Z') + 1:
        return

    for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
        nx, ny = x + dx, y + dy
        if isPromising(nx, ny):
            visited[stoi(board[nx][ny])] = True
            dfs(nx, ny, depth + 1)
            visited[stoi(board[nx][ny])] = False


R, C = map(int, input().split())
board = list(input() for _ in range(R))
visited = [False] * (stoi('Z') + 1)

ans = [0]
visited[stoi(board[0][0])] = True
dfs(0, 0, 1)

print(*ans)
