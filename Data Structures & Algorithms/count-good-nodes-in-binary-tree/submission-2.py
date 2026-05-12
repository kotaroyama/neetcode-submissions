# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maximum):
            if not root:
                return 0
            maximum = max(maximum, root.val)    
            result = 0
            if root.val >= maximum:
                result = 1
            result += dfs(root.left, maximum)
            result += dfs(root.right, maximum)
            return result

        return dfs(root, root.val)