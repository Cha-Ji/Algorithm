#Ex_2502 떡먹는 호랑이 dp[실버1]
days, total = list(map(int, input().split()))

# A B A+B A+B+B A+B+B+A+B
fiboA = 1
fiboB = 1
end = [1,1]
j = 0
for i in range(2, days):
    end[j] = end[0] + end[1]
    j = 1 - j
    if i == days - 2:
        fiboA = end[j]
    if i == days  - 1:
        fiboB = end[j]
        break

for A in range(1, total//fiboA):
    fB = total - A * fiboA
    if fB % fiboB == 0:
        print(A)
        print(fB//fiboB)
        break
