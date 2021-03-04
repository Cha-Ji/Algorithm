# Ex_2630 색종이 만들기 [실3]
def isOneColor(start, width, ans, color):
    # 정지조건
    if width == 1:
        ans[color] += 1
        return ans
    # 통일 여부
    correct = True
    for i in range(width - 1):
        for j in range(width - 1):
            if board[start[0] + i][start[1] + j] != color:
                correct = False
                break

    if color == 1 and correct:
        print(start, width, ans)
    # 통일되었다면 ans 증가
    if correct:
        ans[color] += 1

    # 통일되지 않았다면 4분할 재귀
    else:
        width //= 2
        for dx, dy in (0, 0), (0, width - 1), (width - 1, 0), (width - 1, width - 1):
            start[0] += dx
            start[1] += dy
            nextColor = board[start[0]][start[1]]
            ans = isOneColor(start, width, ans, nextColor)
    return ans


N = int(input())
board = [[0] * N for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))

ans = isOneColor([0, 0], N, [0, 0], board[0][0])

print(ans[0])
print(ans[1])
"""
if not isOneColor([0, 0], N):
    if not isOneColor([0, 0], N/2):
        adf
    isOneColor([N/2, 0], N/2)
    isOneColor([0, N/2], N/2)
    isOneColor([N/2, N/2], N/2)




"""
