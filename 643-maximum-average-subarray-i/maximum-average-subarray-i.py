class Solution(object):
    def findMaxAverage(self, nums, k):
        s = 0
      
        for i in range(k):
            s += nums[i]
        ma = s
        st = 0
        ed = k
        while ed<len(nums):
            s -= nums[st]
            st +=1

            s +=nums[ed]
            ed+=1

            ma  = max(s,ma)
        return float(ma)/k


        

            
             

        
       
        
        