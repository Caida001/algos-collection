Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # use BFS to check path between s and d
    def isReachable(self, s, d):
        # mark all the vertices as not visited
        visited = [False] * self.V

        queue = []

        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # dequeue a vertex from queue
            n = queue.pop(0)

            # if this adjacent node is the destination node, then return true
            if n == d:
                return True

            # else, continue to do BFS
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return False
