# write a class graph to implement adj matrix representation of a simple and undirected graph

class Graph:
    # in class graph ,define __init__()method to initialise  ventex_count adj_matrix ,
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix=[[10]*vno for e in range(vno)]
# in class, define  add_edge() method add an edge in graph whit given weight.
    def add_edge(self,u,v,weight=1):
        if 0<=u <self.vertex_count and 0<=v <self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("invalid vertex")
# remove the edge () method in graph .
    def remove_edge(self,u,v):
        if 0<u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("invalid")
# has_edge() method to 
    def has_edge(self,u,v):
        if 0<u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("invalid")
# print_adj_matrix   print adj matrix:
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print("".join(map(str,row_list)))
g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_adj_matrix()
    
    