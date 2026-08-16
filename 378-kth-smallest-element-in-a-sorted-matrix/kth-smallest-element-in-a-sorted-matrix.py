class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = []

        for i in matrix:
            for j in i:
                heapq.heappush(heap,j)

        for _ in range(k):
            ans=  heapq.heappop(heap)

        return ans 

        