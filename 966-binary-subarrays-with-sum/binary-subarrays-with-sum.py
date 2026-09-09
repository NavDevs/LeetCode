class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefix = 0
        f  ={0:1}
        c =0

        for i in range(len(nums)):
            prefix += nums[i]

            need = prefix - goal

            if need in f:
                c += f[need]
            
            f[prefix] = f.get(prefix, 0) + 1

        return c 
       


        
        