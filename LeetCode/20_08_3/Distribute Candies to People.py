class Solution:
    def distributeCandies(self, candies: int, num_people: int):

        result = [0]*num_people

        index = 0
        givenCandies = 1
        while candies > 0:
            if candies < givenCandies:
                result[index] += candies
                break
            result[index] += givenCandies

            index = (index + 1) % num_people
            candies -= givenCandies
            givenCandies += 1
        return result

a = Solution()
print(a.distributeCandies(7,4))
