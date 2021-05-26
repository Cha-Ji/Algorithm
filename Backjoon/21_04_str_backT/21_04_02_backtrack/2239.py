# Ex_2239 스도쿠 [골4]

# 들어가도 되는 숫자인지
def isPromising(x, y, n):
    return not visitedX[x][n] and not visitedY[y][n] and not visitedBox[x//3 + (y//3) * 3][n]


def dfs(i):
    if i >= len(stack):
        if i == lenS:
            for x in range(9):
                print(''.join(board[x]))
            stack.clear()
        return

    x, y = stack[i]
    for n in range(9):
        if isPromising(x, y, n):
            board[x][y] = str(n + 1)
            visitedX[x][n] = True
            visitedY[y][n] = True
            visitedBox[x//3 + (y//3) * 3][n] = True
            dfs(i + 1)
            board[x][y] = '0'
            visitedX[x][n] = False
            visitedY[y][n] = False
            visitedBox[x//3 + (y//3) * 3][n] = False


board = [[0] * 9 for _ in range(9)]
visitedX = [[False] * 9 for _ in range(9)]
visitedY = [[False] * 9 for _ in range(9)]
visitedBox = [[False] * 9 for _ in range(9)]

stack = []

for x in range(9):
    thisLine = input()
    for y in range(9):
        board[x][y] = thisLine[y]

        if board[x][y] == '0':
            stack.append([x, y])

        else:
            visitedX[x][int(board[x][y]) - 1] = True
            visitedY[y][int(board[x][y]) - 1] = True
            visitedBox[x//3 + (y//3) * 3][int(board[x][y]) - 1] = True
lenS = len(stack)

dfs(0)
