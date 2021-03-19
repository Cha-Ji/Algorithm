# Ex_2504 괄호의 값 [실2]
def search(start, end):
    if start >= end:
        return 1

    openIdx1, openIdx2, couple = [], [], [[-1, -1, -1]]

    # 괄호 쌍 찾기
    for i in range(start, end):
        if l[i] == "(":
            openIdx1.append(i)
        elif l[i] == "[":
            openIdx2.append(i)
        elif l[i] == ")":
            if openIdx1:
                couple.append([openIdx1.pop(), i, 2])
            else:
                return 0
        else:
            if openIdx2:
                couple.append([openIdx2.pop(), i, 3])
            else:
                return 0

    # 올바르지 않은 괄호
    if openIdx1 or openIdx2:
        return 0

    # 독립적인 괄호만 답에 더한다.
    ans = 0
    end = couple[-1]
    for openNode in couple[::-1]:
        if openNode[1] < end[0]:
            ans += end[2] * search(end[0] + 1, end[1])
            end = openNode

    return ans


l = input()
print(search(0, len(l)))
