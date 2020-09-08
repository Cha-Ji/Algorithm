# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root, total_bin):
            if not root:
                result = 0
                reversed_bin = total_bin[:0:-1]
                for i in range(len(reversed_bin)):
                    result += int(reversed_bin[i]) * pow(2,i)
                return result

            next_val = str(total_bin) + str(root.val)
            if not root.left: return dfs(root.right, next_val)
            if not root.right: return dfs(root.left, next_val)
            return dfs(root.left, next_val) + dfs(root.right, next_val)

        return dfs(root, 0)

