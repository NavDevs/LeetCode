class Solution(object):
    def binaryS(self,row,target):
        l = 0
        r  = len(row)-1
        while l <=r:
            m  = (l+r)// 2
            if row[m]==target:
                return True
            elif row[m]<target:
                l = m +1
            else:
                r  = m -1
        return False 
    def searchMatrix(self, matrix, target):
        for row in matrix :
            if self.binaryS(row,target):
                return True
        return False
            
        
        
        