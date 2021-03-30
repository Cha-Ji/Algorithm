# Ex_16903 수열과 쿼리 20 [플2]
import sys
p = sys.stdin.readline
A = [False, False, 0]
for i in range(int(p())+1):
    o, x = (1, 0) if i == 0 else map(int, p().split())
    r = "0b"
    h = A
    for b in format(x, 'b').zfill(30):
        b = int(b)
        if o == 1:
            if h[b]:
                h[b][2] += 1
            else:
                h[b] = [False, False, 0]
        elif o == 2:
            if h[b][2] > 0:
                h[b][2] -= 1
            else:
                h[b] = False
                break
        else:
            if h[b ^ 1]:
                r += '1'
                b ^= 1
            else:
                r += '0'
        h = h[b]
    if o == 3:
        print(int(r, 2))
