#Ex_2437 저울 [골드3]
N = int(input())
w = sorted(list(map(int, input().split())))

# 될때까지 해보자
ans, index = 1, 0

# 무게 1 ~ 1,000,000 측정
while True:
    # ans보다 큰 수를 배제한다.
    for i in range(index, N):
        if ans <= w[i]:
            index = i
            break
        
        if i == N-1:
            index = N-1

    thisAns = ans
    # 큰 수부터 차례로 빼본다.
    for i in w[index::-1]:
        if thisAns >= i:
            thisAns -= i
        
        if thisAns == 0:
            break

    # 무게 조합 성공 or 실패
    if thisAns == 0:ans += 1
    else:break


print(ans)