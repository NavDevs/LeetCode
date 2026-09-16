class Solution(object):
    def topKFrequent(self, words, k):
        m = Counter(words)

        

        heap = []

        for i in m:
            heapq.heappush(heap,(-m[i],i))

       
        a  = []

        for _ in range(k):
            freq,i = heapq.heappop(heap)
            a.append(i)

        return a 


        