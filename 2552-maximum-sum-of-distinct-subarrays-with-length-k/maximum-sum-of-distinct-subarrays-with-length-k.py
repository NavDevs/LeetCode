class Solution(object):
    def maximumSubarraySum(self, nums, k):
        seen  =set()
        cur  = 0 
        maxlen = 0
        l = 0

        for r in range(len(nums)):

            while nums[r] in seen:
                seen.remove(nums[l])
                cur  -= nums[l]
                l +=1

            seen.add(nums[r])
            cur += nums[r]

            if r - l +1 > k:
                seen.remove(nums[l])
                cur -= nums[l]
                l +=1
            
            if r - l + 1 == k:
                maxlen = max(maxlen, cur)

        return maxlen 

            
        
        