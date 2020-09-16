# 신입사원

for _ in range(int(input())):   # testCase
    # input
    score_rank = []
    for __ in range(int(input())):
        score_rank.append(list(map(int, input().split())))
    score_rank.sort()

    stupid = score_rank[0]
    result = 1
    for i in score_rank:
        result += stupid[1] > i[1]
        stupid = [i[0], min(stupid[1], i[1])]
    print(result)

