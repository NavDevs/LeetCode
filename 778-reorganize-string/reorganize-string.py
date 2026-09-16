class Solution(object):
    def reorganizeString(self, s):
        freq = Counter(s)
        heap = []

        for ch, cnt in freq.items():
            heapq.heappush(heap,(-cnt,ch))

        res = []

        while len(heap)>= 2:
            cnt1 , ch1 = heapq.heappop(heap)
            cnt2 , ch2 = heapq.heappop(heap)

            res.append(ch1)
            res.append(ch2)
            
            cnt1 +=1
            cnt2 += 1

            if cnt1 < 0:
                heapq.heappush(heap,(cnt1,ch1))
            
            if cnt2 < 0:
                heapq.heappush(heap,(cnt2,ch2))

        if heap:

            c , ch =  heapq.heappop(heap)
            if c < -1:
                return ""

            res.append(ch)

        return "".join(res)
            
            


       