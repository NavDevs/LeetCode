class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap =[]

        for i in arr:
            heapq.heappush(heap,(abs(i-x),i))
        
        a= []

        for _ in range(k):
            distance , i =  heapq.heappop(heap)
            a.append(i)

        a.sort()

        return a 