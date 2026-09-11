class Solution(object):
    def nextGreaterElements(self, nums):
        st = []
        n = len(nums)
        res = [-1]*n

        for i in range(n*2):
            while st and nums[st[-1]] < nums[i%n]:
                idx  = st.pop()
                res[idx] = nums[i%n]
            st.append(i%n)
        return res 
        