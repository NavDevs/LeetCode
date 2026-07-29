class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        v  = [False]*n
        def dfs(city):
            v[city] = True
            for i in range(n):
                if isConnected[city][i] == 1 and not v[i]:
                    dfs(i)

        p = 0 

        for i in range(n):
            if not v[i]:
                p+=1
                dfs(i)

        return p        
        