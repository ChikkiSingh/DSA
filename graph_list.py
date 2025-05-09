# write a class graph to implement list representation of the graph data structures...;
class graph:
 # define the  __init__()method to initialise instance ohj variable vertex_count and dict obj_list key is vertex no and values is a list pf adjacent variable..
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={v:[]for v in range(vno)}
        
# add_edge() method to add and edge in the graph with given vertices and weight..
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((v,weight))
        else:
            print('invalid vertices') 
# remove the element in adj_list in a graph;
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u]=[(vertex,weight) for vertex ,weight in self.adj_list[u] if vertex!=v]
            self.adj_list[v]=[(vertex,weight)for vertex,weight in self.adj_list[v]if vertex!=u]
        else:
            print('invalid vertices')
# has_edges()method 
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<u<self.vertex_count:
            return any (vertex==v for vertex, x in self.adj_list[u])
        else:
            print('invalid vertices')
            return False
# print adj_list;
    def print_adj_list(self):
        for vertex,n in self.adj_list.items():
            print('v',vertex,':',n)
            
g=graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.print_adj_list()
     
            
        