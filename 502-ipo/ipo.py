import heapq

class Solution(object):

    def findMaximizedCapital(self, k, w, profits, capital):

        maxP = []

        minC = [(c,p) for c , p in zip(capital,profits)]
        heapq.heapify(minC)

        for _ in range(k):

            while minC and minC[0][0] <= w:
                c,p =heapq.heappop(minC)
                heapq.heappush(maxP,-p)

            if not maxP:
                break

            w += -heapq.heappop(maxP)

        return w 