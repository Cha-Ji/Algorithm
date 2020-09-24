class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
            print(n, candidate1, candidate2, count1, count2)
        return [n for n in (candidate1, candidate2)
                    if nums.count(n) > len(nums) // 3]
a = Solution()
print(a.majorityElement([1,2,3,4,5,6,7,8,9,9,9,9,9]))
