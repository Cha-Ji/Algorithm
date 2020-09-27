class Solution:
    def firstMissingPositive(self, nums) -> int:
        small_dict, ans = {}, 1
        for i in nums: small_dict[i] = True
        while small_dict.get(ans): ans += 1
        return ans
a = Solution()
print(a.firstMissingPositive([1,2,3]))