# Ex_1786 찾기: [골1]
def KMP(target):
    ans = []
    prefix = 0
    suffix = 0
    for suffix in range(len(target)):
        # suf == pref가 끊기면 길이를 초기화하며 재검사한다.
        while prefix > 0 and target[suffix] != pat[prefix]:
            # 길이를 초기화할 때 덜 줄인다.
            prefix = pi[prefix - 1]

        # suf == pref를 찾으면 한 칸 더 검사한다.
        if target[suffix] == pat[prefix]:
            prefix += 1
            # 단어가 일치할 때 True를 반환한다.
            if prefix == len(pat):
                start = suffix - prefix + 1
                ans.append(start + 1)

                # 탐색 초기화
                prefix = pi[prefix - 1]
    return ans


txt, pat = input(), input()
pi = [0] * len(pat)
prefix = 0
# 접미사를 기준으로 탐색한다.
for suffix in range(1, len(pat)):
    # suf == pref가 끊기면 길이를 줄여보며 재검사한다.
    while prefix > 0 and pat[suffix] != pat[prefix]:
        # 0 ~ pi만큼의 과정을 생략한다.
        prefix = pi[prefix-1]

    # suf == pref를 찾으면 pref를 한 칸 더 검사하고, pi를 업데이트한다.
    if pat[suffix] == pat[prefix]:
        prefix += 1
        pi[suffix] = prefix

result = KMP(txt)
print(len(result))
if len(result) > 0:
    print(*result)
