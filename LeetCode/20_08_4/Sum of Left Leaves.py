# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def noChild(self, root):
        return root.left is None and root.right is None
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def searchLeft(root):
            if root is None:
                return 0
            if root.left is not None and self.noChild(root.left):
                return root.left.val + searchLeft(root.right)

            return searchLeft(root.left) + searchLeft(root.right)
        return searchLeft(root)
