# Ex_16903 수열과 쿼리 20 [플2]
import sys
input = sys.stdin.readline


def insert():
    cur = A
    for b in binX:
        b = int(b)
        if cur[b]:
            # count ++
            cur[b][2] += 1
        else:
            cur[b] = [False, False, 0]

        cur = cur[b]


def delete():
    cur = A
    for b in binX:
        b = int(b)
        if cur[b][2] > 0:
            # count --
            cur[b][2] -= 1
        else:
            cur[b] = False
            break

        cur = cur[b]


def xor():
    ans = "0b"

    cur = A
    for b in binX:
        b = int(b)
        if cur[b ^ 1]:
            ans += '1'
            b ^= 1
        else:
            ans += '0'

        cur = cur[b]

    print(int(ans, 2))


# 0, 1, count
A = [False, False, 0]

binX = format(0, 'b').zfill(30)
insert()

for i in range(int(input())):
    order, x = map(int, input().split())
    binX = format(x, 'b').zfill(30)

    if order == 1:
        insert()
    elif order == 2:
        delete()
    else:
        xor()
