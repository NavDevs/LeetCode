class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for i in nums:
            count[i] = 1+count.get(i,0)
        
        res =  sorted(count , key = count.get , reverse = True)[:k]

        return  res 
        