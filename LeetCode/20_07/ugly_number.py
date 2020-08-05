class Solution:
    def min(self, a, b, c):
        if a >= b:
            return c if b >= c else b
        else:
            return c if a >= c else a
    def nthUglyNumber(self, n: int) -> int:


        uglyList = [1]*(1700)
        i = 1
        count2 = 0; count3 = 0; count5 = 0

        #create ugly list
        while i < n:
            next = min(uglyList[count2] * 2, uglyList[count3] * 3, uglyList[count5] * 5)
            uglyList[i] = next
            print(uglyList[i])
            if next == uglyList[count2] * 2:
                count2 += 1
            if next == uglyList[count3] * 3:
                count3 += 1
            if next == uglyList[count5] * 5:
                count5 += 1

            i += 1
        return uglyList[n]

a = Solution

print(a.nthUglyNumber(a,n=10))
