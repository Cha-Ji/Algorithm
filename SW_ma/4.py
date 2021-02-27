# 4
def main():
    N = int(input())
    foot = list(map(int, input().split()))

    def walk(start):
        v = [False]*N
        step = start
        ans = 1
        while 1:
            v[step] = True
            step = step + foot[step]
            ans += 1
            if v[step + foot[step]]:
                return ans + 1
    print(max(walk(0), walk(1), walk(2)))


if __name__ == "__main__":
    main()
