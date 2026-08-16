class Solution(object):
    def findKthLargest(self, nums, k):
        heap =[]

        for i in nums:
            heapq.heappush(heap,i)

            while len(heap) >k:
                heapq.heappop(heap)
            
        return heap[0]
        
        