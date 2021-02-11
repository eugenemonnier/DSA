class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
      self.root = None
    
  def __str__(self, branch = 1):
        if not self.root: return 'None'
        self.result = f'({self.root.val})\n'
        def traverse(node, branch):

            self.result +=  '\t' * branch + '└── (' + str(node.val) + ')\n'
            if node.left: traverse(node.left, branch + 1)
            if node.right: traverse(node.right, branch + 1)
            return self.result
        if self.root.left: traverse(self.root.left, branch)
        if self.root.right: traverse(self.root.right, branch)
        return f'{self.result}'
  
  def pre_order(self):
    nodes = list()
    def happy_tree_friend(node):
      if not node: return
      nodes.append(node.val)
      if node.left: happy_tree_friend(node.left)
      if node.right: happy_tree_friend(node.right)
    
    happy_tree_friend(self.root)
    return nodes

  def in_order(self):
    nodes = list()
    
    def happy_tree_friend(node):
      if not node: return
      if node.left: happy_tree_friend(node.left)
      nodes.append(node.val)
      if node.right: happy_tree_friend(node.right)
    
    happy_tree_friend(self.root)
    return nodes
  
  def post_order(self):
    nodes = list()
    def happy_tree_friend(node):
      if not node: return
      if node.left: happy_tree_friend(node.left)
      if node.right: happy_tree_friend(node.right)
      nodes.append(node.val)
    
    happy_tree_friend(self.root)
    return nodes

  def find_max_val(self):
        return self.happy_tree_friend(self.root)

  def happy_tree_friend(self, node, max_val = float('-inf')):
      if not node: return max_val
      if node.left: max_val = self.happy_tree_friend(node.left, max_val)
      if node.val > max_val: max_val = node.val
      if node.right: max_val = self.happy_tree_friend(node.right, max_val)
      return max_val

  def breadth_first(self):
    queue, nodes = list(), list()
    if not self.root: return nodes
    queue.append(self.root)
    while len(queue):
      current = queue[0]
      if current.left: queue.append(current.left)
      if current.right: queue.append(current.right)
      nodes.append(queue[0].val)
      queue.pop(0)
    return nodes

def sprinkler(inlet):
  return sprinkler_helper(inlet.root)
  
def sprinkler_helper(node, usage = 0):
  if not node: return usage
  usage += node.val
  usage = sprinkler_helper(node.left, usage)
  usage = sprinkler_helper(node.right, usage)
  return usage

sprinkler_sys = BinaryTree()
sprinkler_sys.root = Node(35)
sprinkler_sys.root.left = Node(41)
sprinkler_sys.root.left.left = Node(33)
sprinkler_sys.root.left.right = Node(52)
sprinkler_sys.root.right = Node(59)
sprinkler_sys.root.right.left = Node(30)
sprinkler_sys.root.right.right = Node(44)

print(sprinkler(sprinkler_sys))
