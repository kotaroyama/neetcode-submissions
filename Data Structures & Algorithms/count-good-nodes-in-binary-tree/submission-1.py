# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maximum = root.val
        result = 0
        
        def dfs(root, maximum):
            if not root:
                return

            nonlocal result
            maximum = max(maximum, root.val)

            if root.val >= maximum:
                result += 1

            dfs(root.left, maximum)
            dfs(root.right, maximum)
        
        dfs(root, maximum)
        return result