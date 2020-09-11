class Solution:
    # 0을 기준으로 탐색한다.
    def search(self, nums):
        zero_index_list, zero_count = self.zeroPartition(nums)
        result, end = -123456789, 0
        for i in range(zero_count):
            this_product = 1

            # 곱해가면서 최댓값을 찾는다.
            for j in range(end, zero_index_list[i]):
                this_product *= nums[j]
                result = max(this_product, result)

            # 현재 값이 음수일 경우 양수가 될 때 까지 앞에서 나눈다.
            if this_product < 0:
                for j in range(end, zero_index_list[i] - 1):
                    this_product //= nums[j]
                    if this_product > 0:
                        result = max(this_product, result)
                        break
            end = zero_index_list[i] + 1

        if result < 0 and zero_count > 1:
            return 0
        return result

    # 0의 위치를 찾는다.
    def zeroPartition(self, nums):
        zero_index_list = []
        zero_count, end = nums.count(0), 0
        for _ in range(zero_count):
            this_zero = nums.index(0, end)
            end = this_zero + 1
            zero_index_list.append(this_zero)
        return zero_index_list, zero_count

    def maxProduct(self, nums) -> int:
        if not nums:
            return 0
        # 0을 기준으로 곱할 것이므로 맨 뒤에 0을 더한다.
        return self.search(nums + [0])

a = Solution()
print(a.maxProduct([1,0]))
