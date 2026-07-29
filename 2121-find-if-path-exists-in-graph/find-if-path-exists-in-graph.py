class Solution(object):
    def validPath(self, n, edges, source, destination):
        visited = [False] * n 
        graph = [[]for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def  dfs(source):
            if source == destination:
                return True 
            visited[source] = True

            for i in graph[source]:
                if not visited[i]:
                    if dfs(i):
                        return True 
            return False 
        return dfs(source)    
        