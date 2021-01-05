#Ex_11054 가장 긴 바이토닉 수열
# dp에 갇히지 않고 dfs로 풀어보기

#수열 입력
N = int(input())
s = list(map(int, input().split()))

def down(s, list, i):
    # 정지 조건
    if i == len(s):
        return 1

    # 내림차순으로 진행
    if(list[-1] > s[i]):
        return max(
            1 + down(s, list + [s[i]], i+1),
            down(s, list, i+1)
        )

    else:
        return down(s, list, i+1)


def up(s, list, i):
    # 정지 조건
    if(i == len(s)):
        return 1

    # 수열에 오름차순 추가 중
    # 채택 or 미채택
    if(list[-1] < s[i]):
        return max(
            1 + up(s, list + [s[i]], i+1),
            up(s, list, i+1)
        )

    # 다음 숫자가 같으면 미채택
    if list[-1] == s[i]:
        return up(s, list, i+1)

    # 채택하면 내림차순 미채택하면 오름차순
    if(list[-1] > s[i]):
        return max(
            up(s, list, i+1), 
            down(s, list + [s[i]], i+1) + 1
        )  


print(up(s, [0], 0) - 1)
