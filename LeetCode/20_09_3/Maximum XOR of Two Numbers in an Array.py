# 포기
class Solution:
    def findMaximumXOR(self, nums) -> int:
        nums.sort()
        max_xor = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[-i] == nums[j]:
                    continue
                max_xor = max(max_xor, nums[-i] ^ nums[j])
        return max_xor

a = Solution()
print(a.findMaximumXOR([3,10,5,25,2,8]))
