class Solution(object):
    def intersection(self, nums1, nums2):
        s = set(nums1)
        ans = set()
        for i in nums2:
            if i in nums1:
                ans.add(i)
        return list(ans)        