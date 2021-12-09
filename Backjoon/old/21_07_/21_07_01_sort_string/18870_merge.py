# Ex_18870 좌표 압축: [실2] 머지소트
def merge(left, right):
    result = []
    l, r = 0, 0
    lenL, lenR = len(left), len(right)

    while l < lenL and r < lenR:
        # 정복
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    # 한 쪽의 정렬이 끝났을 때
    if l < lenL:
        result += left[l:]

    if r < lenR:
        result += right[r:]

    return result


def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    l = mergeSort(lst[:mid])
    r = mergeSort(lst[mid:])
    return merge(l, r)


answer = [0] * int(input())
x = list(map(int, input().split()))
newX = list(set(x))  # 중복 제거
sortedX = mergeSort(newX)  # 소팅

dictX = {}  # 매핑
for i in range(len(sortedX)):
    dictX[sortedX[i]] = i

for i in range(len(x)):
    answer[i] = dictX[x[i]]
print(*answer)
