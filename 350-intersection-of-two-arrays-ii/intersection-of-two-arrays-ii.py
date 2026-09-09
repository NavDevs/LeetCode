class Solution(object):
    def intersect(self, nums1, nums2):
        res = []

        freq  = Counter(nums1)

        for i in nums2:
            if freq[i] >0:
                res.append(i)
                freq[i] -= 1
            
        return res
        
        