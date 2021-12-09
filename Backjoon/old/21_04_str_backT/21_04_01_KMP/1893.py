# Ex_1893 시저암호: [골1]
import sys
input = sys.stdin.readline


def getPi():
    # 원문 pi
    pref = 0
    pi = [0] * (len(origin) + 1)
    for suff in range(1, len(origin)):
        while pref > 0 and origin[pref] != origin[suff]:
            pref = pi[pref - 1]

        if origin[pref] == origin[suff]:
            pref += 1
            pi[suff] = pref

            if pref == len(origin):
                break
    return pi


def KMP(origin, pwd, pi):
    # 암호문에서 원문 검색
    thisAns = False
    pref = 0
    for suff in range(len(pwd)):
        while pref > 0 and pwd[suff] != origin[pref]:
            pref = pi[pref - 1]

        if pwd[suff] == origin[pref]:
            pref += 1

            if pref == len(origin):
                if thisAns:
                    return False

                else:
                    pref = pi[pref - 1]
                    thisAns = True
    return thisAns


def shift():
    # 원문 시프트
    shifted = [""] * len(origin)
    for i in range(len(origin)):
        next = (seqDict[origin[i]] + 1) % lenQ
        shifted[i] = seq[next]

    return shifted


for _ in range(int(input())):
    seq = input()[:-1]
    origin = input()[:-1]
    pwd = input()[:-1]

    # 시프트 하기 쉽게 dict에 저장
    lenQ = len(seq)
    seqDict = {}
    for i in range(lenQ):
        seqDict[seq[i]] = i

    pi = getPi()

    ans = []
    for i in range(lenQ):
        # 원문에서 탐색
        if KMP(origin, pwd, pi):
            ans.append(i)

        # 시프트
        origin = shift()

    if len(ans) == 0:
        print("no solution")

    elif len(ans) == 1:
        print("unique:", *ans)

    else:
        print("ambiguous:", *ans)
