# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        # bisect : insort
        # from bisect import insort
        # result = []
        # def dfs(root):
        #     if root:
        #         dfs(root.left)
        #         insort(result,root.val)
        #         dfs(root.right)
        # dfs(root1)
        # dfs(root2)
        # return result

        # sort
        result = []
        def dfs(root):
            if root:
                dfs(root.left)
                result.append(root.val)
                dfs(root.right)
        dfs(root1)
        dfs(root2)
        return sorted(result)





