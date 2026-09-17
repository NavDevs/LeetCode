class Solution(object):
    def possibleBipartition(self, n, dislikes):
        color  = [-1] * (n+1)

        graph = [[] for i in range(n+1)]

        for u , v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        q = deque()

        for i in range(1,n+1):

            if color[i] != -1:
                continue

            color[i] = 0
            q.append(i)

            while q:
                node = q.popleft()

                for nei in graph[node]:

                    if color[nei] == -1:
                        q.append(nei)
                        color[nei] = 1 - color[node]

                    elif color[nei] == color[node]:
                        return False

        return True 

        
            
        