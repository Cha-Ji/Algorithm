#sorting
# 떨어지는 개미
def accident(temp_list, p_list, fallen, i):
    if fallen[i+1]:
        return
    if temp_list[i] + p_list[i] > temp_list[i+1] + p_list[i+1]:
            temp_list[i] *= -1
            temp_list[i+1] *= -1

def isFalling(p_list, fallen, i, L):
    if fallen[i]:
        return False

    fallen[i] = p_list[i] < 0 or p_list[i] > L
    return fallen[i]

for _ in range(int(input())):
    N, L, k = map(int, input().split())
    p_list, a_list, temp_list = [], [], []

    for __ in range(N):
        p, a = map(int, input().split())   # ID, 초기 위치
        p_list.append(p)
        a_list.append(a)
        temp_list.append(a)

    #진행
    fallen = [False] * L
    fallen.append(True)
    temp_list.append(True), p_list.append(True)

    while k > 0:
        for i in range(N):
            #충돌
            accident(temp_list, p_list, fallen, i)

            #진행
            p_list[i] += temp_list[i]

            #추락하면 k--
            k -= isFalling(p_list, fallen, i, L)

            print("현재 상황","k = ",k,p_list)
            if k == 0:
                print("as",a_list[i])
                break