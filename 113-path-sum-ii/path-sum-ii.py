class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return []

        if root.left is None  and root.right is None:
            if targetSum == root.val:
                return [[root.val]]
            else:
                return []
        ans = []
        
        for i in self.pathSum(root.left , targetSum-root.val):
            ans.append([root.val]+i)
        for i in self.pathSum(root.right , targetSum-root.val):
            ans.append([root.val]+i)
        
        return ans 
         
        