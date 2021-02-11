class Node:
  def __init__(self, val):
      self.val = val
      self.next = None

class Queue:
  def __init__(self):
      self.front = None
  
  def enqueue(self, val):
    node = Node(val)
    if not self.front: self.front = node
    else:
      curr_node = self.front

      while curr_node.next:
        curr_node = curr_node.next
      curr_node.next = node
  
  def dequeue(self):
    if not self.front: return "Nothing here"
    removed = self.front.val
    self.front = self.front.next
    return removed

  def is_empty(self):
    if self.front: return False
    else: return True

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
    self.adjacencies.get(nodeA).append({'node': nodeB, 'weight' : weight})
    self.adjacencies.get(nodeB).append({'node': nodeA, 'weight' : weight})

  def get_nodes(self):
    return self.nodes

  def get_neighbors(self, node):
    return self.adjacencies.get(node)

  def size(self):
    graph_size = len(self.nodes)
    return graph_size

  def breadth_first(self, node):
    result, visited, node_queue = [], dict(), Queue()
    for key in self.adjacencies.keys():
      visited[key] = False
    visited[node] = True
    node_queue.enqueue(node)

    while not node_queue.is_empty():
      queued_node = node_queue.dequeue()
      neighbor_list = self.adjacencies.get(queued_node)
      for neighbor_map in neighbor_list:
        neighbor = neighbor_map.get('node')
        if not visited[neighbor]:
          visited[neighbor] = True
          node_queue.enqueue(neighbor)
      result.append(queued_node)
    return result

  def get_edge(self, nodeA, nodeB):
    adjacencies = self.adjacencies.get(nodeA)
    for neighbors in adjacencies:
      if nodeB in neighbors: return neighbors[nodeB]
    return LookupError('Edge does not exist.')
  
  def depth_first(self, node):
    if len(self.nodes) == 0: return ValueError('Graph does not contain nodes.')
    visited, output = {}, []
    for nodes in self.nodes: visited[nodes] = False
    if not node in visited.keys(): return ValueError('Node does not exist in graph.')
    self.depth_first_helper(node, visited, output)
    return output

  def depth_first_helper(self, node, visited, output):
    if not visited[node]:
      visited[node] = True
      output.append(node)
      neighbors = self.adjacencies.get(node)
      for neighbor in neighbors: self.depth_first_helper(neighbor['node'], visited, output)
    return output


test_graph = Graph()
test_graph.add_node('A')
test_graph.add_node('B')
print(test_graph.add_node('B'))
test_graph.add_edge('A', 'B', 100)
print(test_graph.add_edge('A', 'B', 100))
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
test_graph.add_edge('C', 'B', 200)
test_graph.add_edge('C', 'G', 150)
test_graph.add_edge('A', 'D', 300)
test_graph.add_edge('B', 'D', 450)
test_graph.add_edge('E', 'D', 90)
test_graph.add_edge('F', 'D', 400)
test_graph.add_edge('H', 'D', 240)
test_graph.add_edge('H', 'F', 420)
print("Breadth First Test")
print(test_graph.breadth_first('A'))
print('Get Edge Tests')
print(test_graph.get_edge('D', 'B'))
print(test_graph.get_edge('A', 'F'))
print()
print('Depth First Test')
print('Empty Graph:')
graph = Graph()
print(graph.depth_first('Jakku'))
graph.add_node('Jakku')
graph.add_node('Takodana')
graph.add_node('Starkiller Base')
graph.add_node('Kijimi')
graph.add_node('Kef Bir')
graph.add_node('Exegol')
graph.add_edge('Jakku', 'Takodana', 200)
graph.add_edge('Kijimi', 'Takodana', 300)
graph.add_edge('Jakku', 'Starkiller Base', 300)
graph.add_edge('Starkiller Base', 'Takodana', 100)
graph.add_edge('Starkiller Base', 'Kijimi', 400)
graph.add_edge('Starkiller Base', 'Kef Bir', 600)
graph.add_edge('Kijimi', 'Kef Bir', 500)
graph.add_edge('Exegol', 'Kef Bir', 1700)
print('Happy Path:')
print(graph.depth_first('Jakku'))
print('Invalid Node:')
print(graph.depth_first('Alderaan'))