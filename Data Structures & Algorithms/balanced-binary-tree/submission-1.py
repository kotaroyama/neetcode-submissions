# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)

        if not leftBalanced or not rightBalanced:
            return False

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False
        else:
            return True
        