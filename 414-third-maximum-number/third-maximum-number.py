import heapq
class Solution(object):
    def thirdMax(self, nums):
        heap = []
        
        
        nums= set(nums)
        for i in nums:
            heapq.heappush(heap,i)

            if len(heap) > 3:
                heapq.heappop(heap)
        if len(heap) < 3:
            return max(heap)
        return heap[0]