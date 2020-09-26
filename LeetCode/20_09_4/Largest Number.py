class Solution:
    def largestNumber(self, nums) -> str:
        max_length = len(str(max(nums)))
        result = ''
        for i in sorted(nums, reverse=True, key=lambda i: str(i)*max_length):
            result += str(i)
        return result if int(result) != 0 else '0'

