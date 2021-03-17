# Ex_1074 Z [실1]
# 시간제한 0.5, 메모리 512
N, r, c = map(int, input().split())


def search(x, y, n, s):
    if x == c and y == r:
        return s

    for dx, dy, i in (x, y, 0), (x + n, y, 1), (x, y + n, 2), (x + n, y + n, 3):
        if dx <= c < dx + n and dy <= r < dy + n:
            return search(dx, dy, n//2, s + n**2 * i)


print(search(0, 0, 2**(N-1), 0))
