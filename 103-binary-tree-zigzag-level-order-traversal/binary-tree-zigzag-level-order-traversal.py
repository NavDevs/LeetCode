# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q  = deque([root])
        ans = []
        ltor = True
        while q :
            l = []
            
            for i in range(len(q)):
                n = q.popleft()
                l.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if not ltor:
                l.reverse()
            ans.append(l)
            ltor   = not ltor
        return ans
        