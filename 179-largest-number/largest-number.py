class Solution(object):
    def largestNumber(self, nums):
        from functools import cmp_to_key

        nums = [str(i) for i in nums]

        def compare(a,b):
            if a + b > b + a:
                return -1
            return 1 

        nums.sort(key= cmp_to_key(compare))

        ans = ''.join(nums)

        if ans[0] == '0':
            return '0'
        
        return ans 
        
        