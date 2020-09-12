class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []
        def dfs(i, total, sum_list: list):
            if total == 0 and len(sum_list) == k: return result.append(sum_list)
            if total > 0 and i != 9:
                dfs(i+1, total - (i + 1), sum_list + [i+1])
                dfs(i+1, total, sum_list)
        dfs(0, n, [])
        return result

a = Solution()
print(a.combinationSum3(3, 9))
