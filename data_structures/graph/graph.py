class Graph:
  def __init__(self):
      self.adjancies = {}
      self.nodes = set()
  
  def add_node(self, val):
    if val in self.nodes: return ValueError('Node already exists.')
    self.nodes.add(val)
    self.adjancies[val] = []
    return val
  
  def add_edge(self, nodeA, nodeB, weight = None):
    if {nodeB : weight} in self.adjancies.get(nodeA): return ValueError('Edge already exists.')
    self.adjancies.get(nodeA).append({nodeB : weight})
    self.adjancies.get(nodeB).append({nodeA : weight})

  def get_nodes(self):
    return self.nodes

  def get_neighbors(self, node):
    return self.adjancies.get(node)

  def size(self):
    graph_size = len(self.nodes)
    return graph_size
  

test_graph = Graph()
test_graph.add_node('A')
test_graph.add_node('B')
print(test_graph.add_node('B'))
test_graph.add_edge('A', 'B', 10)
print(test_graph.add_edge('A', 'B', 10))
print(test_graph.adjancies)
print(test_graph.get_nodes())
print(test_graph.get_neighbors('A'))
print(test_graph.size())


#graph.adjancies = { 'A': [{
#                            'B' : 10,
#                            'C' : 20}]}