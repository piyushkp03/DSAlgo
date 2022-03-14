class Graph:
    def __init__(self, n):
        self.size = n
        self.graph = [[] for i in range(n)]

    def addedge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False for i in range(self.size)]

        queue = []
        queue.append(s)
        visited[s]=True
        print("visited",s)
        while(queue):
            for node in self.graph[s]:
                if not visited[node]:
                    queue.append(node)
                    visited[node]=True
                    print("Visited ",node)
            s=queue.pop(0)









g = Graph(8)
g.addedge(1, 2)
g.addedge(2, 1)
g.addedge(1, 3)
g.addedge(3, 1)
g.addedge(2, 4)
g.addedge(4, 2)
g.addedge(2, 5)
g.addedge(5, 2)
g.addedge(3, 6)
g.addedge(6, 3)
g.addedge(3, 7)
g.addedge(7, 3)
print(g.graph)
g.bfs(1)

