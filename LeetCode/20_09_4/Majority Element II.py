class Solution:
    def majorityElement(self, nums):
        ans = []
        for i in set(nums):
            if nums.count(i) > len(nums) // 3:
                ans.append(i)
        return ans
a = Solution()
print(a.majorityElement([1,1,1,2,2,3,3,3]))
