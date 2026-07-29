class Solution(object):
    def findCenter(self, edges):
        n =  len(edges)+ 1
        d = [0] * (n+1)

        for u , v in edges:
            d[u] +=1
            d[v] +=1
        
        return d.index(max(d))