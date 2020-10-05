class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return N ^max(( (1 << N.bit_length()) - 1), 1)
a = Solution()
print(a.bitwiseComplement(0))