class Solution(object):
    def topKFrequent(self, nums, k):
        m = {}

        m = Counter(nums)
        heap =[]

        for i in m:
            heapq.heappush(heap, (m[i],i))

            if len(heap) > k:
                heapq.heappop(heap)
            

        return [i for freq,i in heap]
        
        