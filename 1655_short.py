import bisect
a = []
for i in range(int(input())):
    bisect.insort(a, int(input()))
    print(a[i//2])
