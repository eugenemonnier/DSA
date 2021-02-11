class Graph:
  def __init__(self):
      self.adjacencies = {}
      self.nodes = set()
  
  def add_node(self, val):
    if val in self.nodes: return ValueError('Node already exists.')
    self.nodes.add(val)
    self.adjacencies[val] = []
    return val
  
  def add_edge(self, nodeA, nodeB, weight = None):
    if {nodeB : weight} in self.adjacencies.get(nodeA): return ValueError('Edge already exists.')
    self.adjacencies.get(nodeA).append({nodeB : weight})
    self.adjacencies.get(nodeB).append({nodeA : weight})

  def get_nodes(self):
    return self.nodes

  def get_neighbors(self, node):
    return self.adjacencies.get(node)

  def size(self):
    graph_size = len(self.nodes)
    return graph_size
  
  def breadth_first(self, node):
    queue, output, visited = [], [], []
    queue.append(node)
    visited.append(queue[0])
    while queue:
      adjacencies = self.adjacencies.get(queue[0])
      for neighbors in adjacencies: 
        for neighbor in neighbors:
          if not neighbor in visited:
            queue.append(neighbor)
            visited.append(neighbor)
      output.append(queue[0])
      queue.pop(0)
      
    return output
  

test_graph = Graph()
test_graph.add_node('A')
test_graph.add_node('B')
print(test_graph.add_node('B'))
test_graph.add_edge('A', 'B', 10)
print(test_graph.add_edge('A', 'B', 10))
print(test_graph.adjacencies)
print(test_graph.get_nodes())
print(test_graph.get_neighbors('A'))
print(test_graph.size())
test_graph.add_node('C')
test_graph.add_node('D')
test_graph.add_node('E')
test_graph.add_node('F')
test_graph.add_node('G')
test_graph.add_node('H')
test_graph.add_edge('C', 'B')
test_graph.add_edge('C', 'G')
test_graph.add_edge('A', 'D')
test_graph.add_edge('B', 'D')
test_graph.add_edge('E', 'D')
test_graph.add_edge('F', 'D')
test_graph.add_edge('H', 'D')
test_graph.add_edge('H', 'F')
print(test_graph.breadth_first('A'))
