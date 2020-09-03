class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        # 예외 처리
        if not nums or k == 0:
            return False

        length = len(nums)

        # nums에서 인덱스와 값이 뒤바뀐 dict를 만든다.
        dict_list = {}; check_overlap = {}
        for i in range(length):
            # 중복을 따지기 위해 만든 배열
            if nums[i] in dict_list.keys():
                check_overlap[nums[i]] = i, dict_list[nums[i]]
            else:
                dict_list[nums[i]] = i

        # nums를 정렬해 반복 횟수를 줄인다.
        sorted_list = sorted(nums)

        for i in range(length - 1):
            # t조건
            if sorted_list[i+1] - sorted_list[i] <= t:

                for j in range(i+1, length):

                    # t조건 위반
                    if sorted_list[j] - sorted_list[i] > t:
                        break

                    # 중복된 인덱스일 때, k조건
                    if sorted_list[j] == sorted_list[i]:
                        if abs(check_overlap[sorted_list[i]][0] - check_overlap[sorted_list[i]][1]) <= k:

                            return True

                    # k조건
                    elif abs(dict_list[sorted_list[j]] - dict_list[sorted_list[i]]) <= k:
                        return True

        return False
a = Solution()
print(a.containsNearbyAlmostDuplicate([0,10,22,15,0,5,22,12,1,5], 3, 3))
