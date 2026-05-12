# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []
        queue = deque()

        level = 0
        queue.append(root)
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    if curr.right:
                        queue.append(curr.right)
                    if curr.left:
                        queue.append(curr.left)
            result.append(level[0])
        
        return result