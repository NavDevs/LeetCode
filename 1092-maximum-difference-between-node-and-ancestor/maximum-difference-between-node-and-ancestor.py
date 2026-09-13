# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        def dfs(root,mx,mn):

            if not root:
                return mx - mn

            mx = max(mx,root.val)
            mn = min(mn,root.val)

            l = dfs(root.left,mx,mn)
            r = dfs(root.right,mx,mn)

            return max(l,r)

        return dfs(root,root.val,root.val)
            
            
        