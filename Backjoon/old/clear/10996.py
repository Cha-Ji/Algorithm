#Ex 10996
# for 별찍기 21

# 1 : *
# 2 : *
#      *
N = int(input())

for i in range(N):
    # 홀수줄
    for j in range(N):
        if j%2:print(' ',end='')
        else:print('*',end='')
    print()
    # 짝수줄
    for j in range(N):
        if j%2:print('*',end='')
        else:print(' ',end='')
    print()
