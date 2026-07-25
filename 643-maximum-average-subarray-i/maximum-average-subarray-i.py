class Solution(object):
    def findMaxAverage(self, nums, k):
        s = 0
        for i in range(k):
            s +=nums[i]
        
        st  = 0 
        ed  = k
        maxS = s 

        while ed < len(nums):

            s-= nums[st]
            st +=1 

            s+= nums[ed]
            ed +=1

            maxS = max(maxS,s)

        return maxS/float(k)

      
        