
class Solution:
    def getRow(self, rowIndex: int):
        def nCr(n, r):
            ncr = 1
            for i in range(r):
                ncr *= (n - i) / (r - i)
            return round(ncr)

        result = []
        for i in range(rowIndex + 1):
            result.append(int(nCr(rowIndex, i)))

        return result



a = Solution()
print(a.getRow(7))
