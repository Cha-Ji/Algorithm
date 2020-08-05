class Solution:
    def singleNumber(self, nums):
        nums.sort()
        leng = len(nums) - 2
        delNum = nums[-1]
        while leng > -1:
            if nums[leng] == delNum:
                nums.remove(delNum)
                nums.remove(delNum)
            else:
                delNum = nums[leng]
            leng -= 1
        return nums

a = Solution
print(Solution.singleNumber(a,nums=[1, 2, 1, 3, 5, 2]))


