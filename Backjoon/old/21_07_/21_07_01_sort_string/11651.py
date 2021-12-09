# Ex_11651 좌표 정렬하기 2: [실5]

def merge(left, right):
    result = []

    l, r = 0, 0
    lenL, lenR = len(left), len(right)

    while l < lenL and r < lenR:
        if left[l][1] < right[r][1]:
            result.append(left[l])
            l += 1
        elif left[l][1] == right[r][1]:
            if left[l][0] < right[r][0]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        else:
            result.append(right[r])
            r += 1
    
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

a = [list(map(int, input().split())) for _ in range(int(input()))]
a = mergeSort(a)
# a = sorted([list(map(int, input().split()))
            # for _ in range(int(input()))], key=lambda x: (x[1], x[0]))
for i in a:
    print(*i)
