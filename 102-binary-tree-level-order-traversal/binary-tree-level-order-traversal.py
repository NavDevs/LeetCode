# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def levelOrder(self, root):
        if root is None:
            return []

        q  = deque([root])
        a  = []
        while q:
            l =[]
            for i in range(len(q)):
                n = q.popleft()
                l.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            a.append(l)
        return a 
        
        