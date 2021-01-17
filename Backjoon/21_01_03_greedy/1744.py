#Ex_1744 수 묶기[골드4]
N = int(input())
s_plus = []
s_minus = []
isOne = 0
for i in range(N):
    n = int(input())
    if n == 1:
        isOne += 1
    elif n > 0:
        s_plus.append(n)
    else:
        s_minus.append(n)

# 절댓값이 큰 수부터 묶는다.
def sol(s):
    if len(s) == 0:return 0
        
    ans = 0 if len(s) % 2 == 0 else s[-1]

    for i in range(1, len(s), 2):
        ans += s[i] * s[i-1]

    return ans


print(
    sol(sorted(s_minus)) + 
    sol(sorted(s_plus)[::-1]) + isOne)
    


