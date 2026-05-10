# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.vals = []
        self.counter = 0

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root):
            self.counter += 1
            if not root:
                
                return
            

            left_or_right = self.counter % 2 
            dfs(root.left)
            self.vals.append((root.val, left_or_right))
            print(self.counter)
            dfs(root.right)
    
        dfs(p)
        self.counter = 0
        dfs(q)
        print(self.vals)
        if self.vals[:len(self.vals)//2] == self.vals[len(self.vals)//2:]:
            return True
    
        return False
        
        
