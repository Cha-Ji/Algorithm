# Ex 1912. 연속합

# n개의 수열을 입력 받는다.
n = int(input())
num_list = list(map(int, input().split()))

# dp 테이블을 만든다.
d = [0] * (n+1)
d[0] = num_list[0]

# 수열의 정수 n을 테이블에 넣을지 결정한다.
# 보텀 업 디피를 사용한다.
for i in range(1, n):
    d[i] = max(d[i-1] + num_list[i], d[i])

if(max(d) == 0):
    print(max(num_list))
else:
    print(max(d))



