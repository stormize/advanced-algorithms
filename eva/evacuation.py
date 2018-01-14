class Graph :
    def __init__(self,graph):
        self.graph=graph
        self.row=len(graph[1])
    def BFS(self,source,destination,path):
        visited=[False]*self.row
        queue=[]
        queue.append(source)
        visited[source]=True
        while queue:
            u=queue.pop(0)
            for ind,v in enumerate (graph[u]):
                print(ind)
                if visited[ind]==False and v >0:
                    queue.append(ind)
                    visited[ind]=True
                    path[ind]=u
        print(path,1)
        return True if visited[destination] else False




    def ford(self,source,destination):
        path=[-1]*(self.row)
        max_flow=0
        while self.BFS(source,destination,path):
            path_flow=float("inf")
            s=destination
            while(s!=source):
                path_flow=min(path_flow,self.graph[path[s]][s])
                s=path[s]
            max_flow += path_flow
            v=destination
            while(v!= source):
                u=path[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] +=path_flow
                v = path[v]
        return max_flow


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
n = input().split(" ")
go=[[0 for x in range(int(n[0]))]for y in range (int(n[0]))]
print(go)
for i in range (0,int(n[1])):
    temp = []
    temp=input().split(" ")
    go[int(temp[0])][int(temp[1])]=int(temp[2])

print(go)
g = Graph(go)


source = 0;
sink = len(go)

print("The maximum possible flow is %d " % g.ford(source, sink))