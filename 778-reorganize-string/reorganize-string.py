class Solution(object):
    def reorganizeString(self, s):
        freq  = Counter(s)
        heap = []

        for i ,cnt in freq.items():
            heapq.heappush(heap,(-cnt,i))

        res =[]
        
        while len(heap) >=2:
            c1 , chr1 = heapq.heappop(heap)
            c2 , chr2 = heapq.heappop(heap)

            res.append(chr1)
            res.append(chr2)
            
            c1 +=1
            c2 +=1

            if c1 <0:
                heapq.heappush(heap,(c1,chr1))
            
            if c2 <0:
                heapq.heappush(heap,(c2,chr2))

        if heap:
            c , ch = heapq.heappop(heap)

            if c < -1:
                return ""
            
            res.append(ch)
        
        return "".join(res)
            

       