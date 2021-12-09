# Ex_9253 스페셜 저지: [실3]
def getPi():
    prefix = 0
    # 접미사를 기준으로 탐색한다.
    for suffix in range(1, len(pat)):
        # suf == pref를 찾으면 pref를 한 칸 더 검사하고, pi를 업데이트한다.
        if pat[suffix] == pat[prefix]:
            prefix += 1
            pi[suffix] = prefix

        # suf == pref가 끊기면 길이를 줄여보며 재검사한다.
        while prefix > 0 and pat[suffix] != pat[prefix]:
            # 0 ~ pi만큼의 과정을 생략한다.
            prefix = pi[prefix-1]


def KMP(target):
    prefix = 0
    for suffix in range(len(target)):
        # suf == pref를 찾으면 한 칸 더 검사한다.
        if target[suffix] == pat[prefix]:
            prefix += 1
            # 단어가 일치할 때 True를 반환한다.
            if prefix == len(pat):
                return True

        # suf == pref가 끊기면 길이를 줄이며 재검사한다.
        while prefix > 0 and target[suffix] != pat[prefix]:
            # 0 ~ pi만큼의 과정을 생략한다.
            prefix = pi[prefix - 1]

    return False


A, B, pat = input(), input(), input()
pi = [0] * len(pat)
getPi()
print("YES" if KMP(A) and KMP(B) else "NO")
