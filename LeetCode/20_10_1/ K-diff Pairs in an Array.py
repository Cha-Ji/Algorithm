class Solution:
    def findPairs(self, nums, k: int) -> int:
        import queue

        # O(nlogn)
        nums.sort()

        ans, i, length= 0, 0, len(nums)
        end = nums[0] - 1
        q = queue.deque()

        while i < length:
            # 덱의 왼쪽에서 뽑아 num과 비교한다.
            if q:
                this_k_diff = q.popleft()

                # 채택되었다면, 이전에 채택되었던 요소인지 확인한다.
                if nums[i] - this_k_diff == k:
                    if end == this_k_diff:
                        continue
                    else:
                        end = this_k_diff
                        ans += 1

                # 채택되지 않았다면 요소를 돌려놓는다.
                elif nums[i] - this_k_diff < k:
                    q.appendleft(this_k_diff)
                    
                # 채택될 수 없다면 요소를 버리고 재검사한다.
                else:
                    continue
            q.append(nums[i])
            i += 1
        return ans
a = Solution()
print(a.findPairs([1,2,3,4,5], 1))