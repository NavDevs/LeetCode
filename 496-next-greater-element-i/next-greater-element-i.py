class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        num1idx = { n :i for i,n in enumerate(nums1) }
        stack  =[]
        res =[-1] * len(nums1)

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                indx = num1idx[val]
                res[indx] = cur 
            if cur in nums1:
                stack.append(cur)
        return res 
        
        