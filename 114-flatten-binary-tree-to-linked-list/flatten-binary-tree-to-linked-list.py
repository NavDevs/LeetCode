# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        self.p = None
        def dfs(root):
            if root is None:
                return 

            dfs(root.right)
            dfs(root.left)

            root.right = self.p
            root.left = None
            self.p = root
        dfs(root)
        

    

            
        
        