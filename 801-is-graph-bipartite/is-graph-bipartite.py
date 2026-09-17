class Solution(object):
    def isBipartite(self, graph):
        color= [-1] * len(graph)

        q = deque()

        for i in range(len(graph)):
        
            if color[i] != -1:
                continue

            color[i] = 0
            q.append(i)

            while q:

                node =  q.popleft()

                for nei in graph[node]:

                    if color[nei] == -1:
                        q.append(nei)
                        color[nei] = 1 - color[node]

                    elif color[nei] == color[node]:
                        return False

        return True

        