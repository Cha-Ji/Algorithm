# Ex_5525 IOIOI [실2]
def reset(ans):
    if cnt >= N: ans += cnt - N + 1
    return ans, -1 + start

N = int(input())
input()

char = ['I', 'O']
ans, cnt = 0, -1
start = False
for s in input():
    if s == char[not True]:
        if start == True:
            ans, cnt = reset(ans)
        else:
            cnt += not start
        start = True

    elif s == char[not False]:
        if start == False:
            ans, cnt = reset(ans)
        else:
            cnt += not start
        start = False
print(reset(ans)[0])
