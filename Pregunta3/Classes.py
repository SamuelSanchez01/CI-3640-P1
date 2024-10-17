class Vertex:
    '''
        Class that defines a vertex that will bbe used on a graph
    '''
    def __init__(self, data, n):
        self.data = data
        self.number = n

class Edge:
    '''
        Class that defines a edge that will bbe used on a graph       
    '''
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Graph:
    def __init__(self, vertices):
        '''
            Graph Class
        '''
        self.verticesNumber = len(vertices) #Number of vertices of the graph
        self.Edges = [] # Edges of the Graph
        self.vertices = vertices #Vertices of the Graph
        self.adyacencies = {v : [] for v in vertices} #Adjacencies of the Graph

    def addEdge(self, v1, v2):
        '''
            This method adds an edge to the graph
        
            Input: v1 v2: Vertex
        '''
        newEdge = Edge(v1,v2)
        self.Edges.append(newEdge)
        self.adyacencies[v1].append(v2)

    def BFS(self, start: Vertex, finish: Vertex = "LOCAL"):
        '''
            BFS to check if there is a way from Start to finish
        
        '''
        visited = [False for i in range(self.verticesNumber)]
  
        #Queue for bfs
        queue = []
  
        queue.append(start)
        visited[start.number] = True
  
        while queue:
 
            n = queue.pop(0)
             
            if n.data == finish:
                   return True
 
            for i in self.adyacencies[n]:
                if visited[i.number] == False:
                    queue.append(i)
                    visited[i.number] = True
        return False
    
class Interpreter:
    '''
        Class that represent the interpreters
    '''
    def __init__(self, languageInter, language):
        self.language = language
        self.languageInter = languageInter
    
class Program:
    '''
        Class that represent the programs
    
    '''
    def __init__(self, name, language):
        self.name = name
        self.language = language
    
class Translator:
    '''
        Class that represente the translators
    '''
    def __init__(self, languageTrans, languageFrom, languageTo):
        self.languageTrans = languageTrans
        self.languageFrom = languageFrom
        self.languageTo = languageTo