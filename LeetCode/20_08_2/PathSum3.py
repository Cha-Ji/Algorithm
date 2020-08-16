# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isPossible(self,root,sum):
        return root.val <= sum

    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result = 0

        def isCorrect(root, sum):
            if root == None:
                return
            elif root.val == sum:
                self.result += 1

            isCorrect(root.left, sum - root.val)
            isCorrect(root.right, sum - root.val)

        def searchStartPoint(root, sum):
            if root == None:
                return
            isCorrect(root, sum)
            searchStartPoint(root.left, sum)
            searchStartPoint(root.right, sum)

        searchStartPoint(root, sum)

        return self.result


