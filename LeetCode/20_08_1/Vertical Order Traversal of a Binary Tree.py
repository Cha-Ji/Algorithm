# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        def dfs(root, level, rootList, rootIndex):
            try: root.val
            except: return
            rootList.append(root.val)
            rootIndex.append(level)
            dfs(root.left, level - 1, rootList, rootIndex)
            dfs(root.right, level + 1, rootList, rootIndex)

        rootList = []
        rootIndex = []
        dfs(root,0, rootList, rootIndex)

        minIndex = min(set(rootIndex))
        maxIndex = max(set(rootIndex))

        for i in range(len(rootIndex)):
            rootIndex[i] -= minIndex

        result = [[-1]] * (maxIndex - minIndex + 1)

        for i in range(len(rootList)):
            if result[rootIndex[i]][0] > -1:
                result[rootIndex[i]].append(rootList[i])
                result[rootIndex[i]] = sorted(result[rootIndex[i]])
            else:result[rootIndex[i]] = [rootList[i]]

        return result
