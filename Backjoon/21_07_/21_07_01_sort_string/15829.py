# Ex_15829 Hashing [브2]
def pow(alpha, n, r):
    alpha = ord(alpha) - ord('a') + 1
    for _ in range(r):
        alpha *= n
        alpha %= M
    return alpha
r = 31
M = 1234567891

L = int(input())
S = input()

ans = 0
for i in range(L):
    ans += pow(S[i], r, i)
    ans %= M    
print(ans)