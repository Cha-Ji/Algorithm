# dp 해볼것
class Solution:
    def dfs(self, i, nums) -> int:
        if i >= len(nums):return 0

        this_num = [0] * 4
        for j in range(4):
            if i+j >= len(nums):break
            this_num[j] = nums[i+j]
        this_num[1] = max(this_num[1], this_num[0])

        return max(this_num[0] + this_num[2] + self.dfs(i+4, nums),
                   this_num[1] + this_num[3] + self.dfs(i+5, nums))

    def rob(self, nums) -> int:
        return self.dfs(0, nums)

a = Solution()
print(a.rob([1,2,3,1]))
