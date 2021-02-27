# 2번
import sys
input = sys.stdin.readline


def main():
    p, n, h = map(int, input().split())
    dp = [0]*(p+1)
    time = [[]for _ in range(p+1)]
    for i in range(n):
        x, y = map(int, input().split())
        time[x].append(y)

    # 만들 수 있는 합 중 h이하의 최대
    def dynamicP(timeList):
        timeList.sort()
        result = 0

        for i in range(len(timeList)):
            if result + timeList[i] > h:
                break
            result += timeList[i]

        return result

    index = 1
    for i in time[1:]:
        dp[index] = dynamicP(i)
        index += 1

    for i in range(1, p+1):
        print(i, dp[i]*1000)


if __name__ == "__main__":
    main()
