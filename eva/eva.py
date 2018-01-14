class vertex :
    def __init__(self,name,source=False,sink=False):
        self.name=name
        self.source=source
        self.sink=sink
class edge:
    def __init__(self,start,end,capacity):
        self.start=start
        self.end=end
        self.capacity=capacity
        self.flow=0
        self.return_ednge=None
class flow_network:
    def __init__(self):
        self.vertices=[]
        self.network={}
    def getVertex(self,name):
        for vertex in self.vertices:
            if vertex.name==name:
                return vertex



    def getSink(self):
        for vertex  in self.vertices:
            if vertex.sink==True:
                    return vertex
        return None
    def getSource(self):
        for vertex  in self.vertices:
            if vertex.source==True:
                    return vertex
        return None
    def vertixInNetwork(self,name):
        for vertex in self.vertices:
            if vertex.name==name:
                return vertex
        return False
    def getEdges(self):
        allEdges=[]
        for vertex in self.network:
            for edge in self.network[vertex]:
                allEdges.append(edge)
        return allEdges
    def addVertix(self,name,source=False,sink=False):
        if source==True and sink ==True:
            return "source is sink"
        if self.vertixInNetwork(name):
            return "vertix alrdy exist"
        if source==True:
            if self.getSource() !=None:
                return "source alrdy exist"
        if sink ==True:
            if self.getSink() !=None:
                return "source alrdy exist"
        newVertex = vertex(name,source,sink)
        self.vertices.append(newVertex)
        self.network[newVertex.name]=[]

    def addEdge(self,start,end,capasity):
        if start ==end:
            return "start == end"
        if self.vertixInNetwork(start) ==False:
            return "start not exist"
        if self.vertixInNetwork(end) ==False:
            return "start not exist"
        newEdge=edge(start,end,capasity)
        returnEdge=edge(end,start,0)
        newEdge.return_ednge=returnEdge
        returnEdge.return_ednge=newEdge
        vertex=self.getVertex(start)
        self.network[vertex.name].append(newEdge)
        returnVertex=self.getVertex(end)
        self.network[returnVertex.name].append(returnEdge)
    def getPath(self,start,end,path):
        if start==end:
            return path
        for edge in self.network[start]:
            




