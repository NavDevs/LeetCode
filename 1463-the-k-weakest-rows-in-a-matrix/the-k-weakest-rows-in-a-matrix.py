class Solution(object):
    def kWeakestRows(self, mat, k):
        heap = []

        for i in range(len(mat)):
            sol =  sum(mat[i])
            heapq.heappush(heap,(sol,i))
        
        ans =[]

        for _ in range(k):
            sol ,i = heapq.heappop(heap)
            ans.append(i)
        
        return ans 
        