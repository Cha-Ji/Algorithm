# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        result =[]


        # 중위순회
        def dfs(root1, root2):
            # 더 작은 val을 갖는 root를 먼저 넣는다.
            if not root1 and not root2:
                return
            if not root1:
                min_root = root2
                max_root = root1
            elif not root2:
                min_root = root1
                max_root = root2
            else:
                min_root = min(root1, root2, key=lambda x: x.val)
                max_root = max(root1, root2, key=lambda x: x.val)
            dfs(min_root.left, max_root)
            result.append(min_root.val)
            dfs(min_root.right, max_root)



        dfs(root1,root2)
        print(result)

a = Solution()
a.getAllElements()

