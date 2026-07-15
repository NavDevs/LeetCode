class Solution(object):
    def minSubArrayLen(self, target, nums):
        l= 0 
        s=0
        a = []
        m= float("inf")
        for r in range(len(nums)):
            s += nums[r]

            while s >= target:
                cur = r - l +1
                m = min(m,cur)
                s-=nums[l]
                l+=1
        if m == float("inf"):
            return 0 
        return m

        



        
        