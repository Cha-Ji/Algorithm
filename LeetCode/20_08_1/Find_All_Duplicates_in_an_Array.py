# O(n)
class Solution:
    def findDuplicates(self, nums):
        count = {}      #dict
        result = []     #result list

        #if twice : count[i] = 2
        for i in nums:
            try: count[i] += 1
            except: count[i] = 1
            
        for i in set(nums):
            if count[i] == 2:
                result.append(i)
        return result
print(Solution.findDuplicates(Solution,[4,3,2,7,8,2,3,1]))
