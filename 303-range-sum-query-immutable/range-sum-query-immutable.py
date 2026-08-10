class NumArray(object):

    def __init__(self, nums):
        self.prefix = [0]
        for i in nums:
            self.prefix.append(self.prefix[-1] + i)
        

    def sumRange(self, left, right):
        s = self.prefix[right+1] - self.prefix[left]
        return s  
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)