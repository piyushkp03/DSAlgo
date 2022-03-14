class Graph:
    def __init__(self,n):
        self.size=n
        self.graph=[[] for i in range(n)]
    def addedge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,s):

        stack=[]
        stack.append(s)

        visited=[False for i in range(self.size)]
        while(len(stack)):
            s=stack[-1]
            stack.pop()
            if not visited[s]:
                print("Visited",s)
                visited[s]=True

            for node in self.graph[s]:
                if not visited[node]:
                    stack.append(node)








g=Graph(8)
g.addedge(1,2)
g.addedge(2,1)
g.addedge(1,3)
g.addedge(3,1)
g.addedge(2,4)
g.addedge(4,2)
g.addedge(2,5)
g.addedge(5,2)
g.addedge(3,6)
g.addedge(6,3)
g.addedge(3,7)
g.addedge(7,3)
print(g.graph)
g.dfs(1)

