class Vertex:
  
  def __init__(self,key): #constructor properties
    self.id = key
    self.connectedTo = {}

  def addNeighbor(self,vert,weight=0):
    self.connectedTo[vert] = weight

  def __str__(self):
    return str(self.id) + ' connectedTo: ' + str([x.getId() for x in self.connectedTo])

  def getConnections(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self,nbr):
    return self.connectedTo[nbr]

  def __repr__(self):
    return self.__str__()

class Graph:
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0

  def addVertex(self,key):
    self.numVertices = self.numVertices + 1
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex

  def getVertex(self,key):
    if key in self.vertList:
      return self.vertList[key]
    else:
      return None

  # def __contains__(self,n):
  #   return n in self.vertList

  def addEdge(self,src,dest,weight=0):
    if src not in self.vertList:
      nv = self.addVertex(src)
    if dest not in self.vertList:
      nv = self.addVertex(dest)
    self.vertList[src].addNeighbor(self.vertList[dest], weight)

  def getVertices(self):
    return self.vertList.keys()

  def __iter__(self):
    return iter(self.vertList.values())

g = Graph()
for i in range(6):
  g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

print g.getVertices()

t = g.getVertex(0)
print t.getConnections()

# for v in g.vertList.values():
#   for w in v.getConnections():
#     print("( %s , %s )" % (v.getId(), w.getId()))

# print t
# for x in t.getConnections():
#   print x
  # print "weight : ",t.getWeight(x)