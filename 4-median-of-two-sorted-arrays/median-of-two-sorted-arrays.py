class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        new = nums1 + nums2
        new.sort()

        n = len(new)
        if n % 2 == 0:
            return (new[n//2] + new[n//2 - 1]) / 2.0
        else:
            return float(new[n//2])