# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, minimum, maximum):
            if not root:
                return True

            result = True
            if root.val >= maximum or root.val <= minimum:
                result = False

            result = result and dfs(root.left, minimum, root.val) and dfs(root.right, root.val, maximum)
            return result

        return dfs(root, -math.inf, math.inf)

        
