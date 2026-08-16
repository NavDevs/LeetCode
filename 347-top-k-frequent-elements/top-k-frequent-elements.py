class Solution(object):
    def topKFrequent(self, nums, k):
        m = {}

        for i in nums:
            m[i] = m.get(i,0)+1

        heap =[]

        for i in m:
            heapq.heappush(heap, (m[i],i))

            while len(heap) > k:
                heapq.heappop(heap)
            

        a  = []

        for freq ,i in heap:
            a.append(i)
        
        return a