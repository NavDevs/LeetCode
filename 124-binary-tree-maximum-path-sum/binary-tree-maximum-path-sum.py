# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        ans= [root.val]

        def dfs(root):

            if not root:
                return 0

            l = max(0,dfs(root.left))
            r = max(0,dfs(root.right))

            ans[0] = max(ans[0],root.val+l+r)

            return root.val + max(l,r)

        dfs(root)
        return ans[0]
        
        