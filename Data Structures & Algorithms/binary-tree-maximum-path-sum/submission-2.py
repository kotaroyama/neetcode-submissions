# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        count = float('-inf')
        
        def dfs(node):
            nonlocal count
            if not node:
                return 0

            left_count = 0
            right_count = 0
            if node.left:
                left_count = max(0, dfs(node.left))
            if node.right:
                right_count = max(0, dfs(node.right))
            local_count = node.val + left_count + right_count
            count = max(count, local_count)
            return node.val + max(left_count, right_count)
     
        dfs(root)
        return count