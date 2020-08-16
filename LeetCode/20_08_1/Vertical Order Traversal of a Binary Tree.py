# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode):
        def createTree(parent,child):
            parent.left = child

        root[0].left = root[1]
        root[0].right = root[2]
        root[1].left = root[3]
        root[1].right = root[4]

        result = []
        return result

test = Solution()
test.verticalTraversal([3,9,20,None,None,15,7])
