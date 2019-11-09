# Ex_11729
# recursion
# hanoi tower
def hanoi(n, One, Two, Three):
    if (n == 1):
        print(One, Three)
    else:
        hanoi(n - 1, One, Three, Two)
        print(One, Three)
        hanoi(n - 1, Two, One, Three)

n = int(input())
print(pow(2, n) - 1)
hanoi(n, 1, 2, 3)
