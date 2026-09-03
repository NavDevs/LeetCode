"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        v = {}

        def dfs(node):
            if  node in v:
                return v[node]

            newNode = Node(node.val)
            v[node] = newNode

            for i in node.neighbors:
                newNode.neighbors.append(dfs(i))

            return newNode
        return dfs(node)
        
        