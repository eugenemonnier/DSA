class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
      self.root = None
  
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
    

class BinarySearchTree(BinaryTree):
  def __init__(self):
      super().__init__()

  def add(self, val, curr_node = None):
    if not curr_node: curr_node = self.root
    if not self.root:
      self.root = Node(val)
      return self.root
    
    if curr_node.val == val: return None
    if curr_node.val > val and not curr_node.left:
      curr_node.left = Node(val)
      return curr_node.left
    elif curr_node.val < val and not curr_node.right:
      curr_node.right = Node(val)
      return curr_node.right
    
    if curr_node.val > val: self.add(val, curr_node.left)
    if curr_node.val < val: self.add(val, curr_node.right)

  def contains(self, val):
    curr_node = self.root
    while True:
      if curr_node.val > val:
        if curr_node.left: curr_node = curr_node.left
        else: return False
      elif curr_node.val < val:
        if curr_node.right: curr_node = curr_node.right
        else: return False
      else: return True

test_tree = BinarySearchTree()
test_tree.add(10)
test_tree.add(5)
test_tree.add(14)
test_tree.add(15)
test_tree.add(11)
test_tree.add(1)
print(test_tree.pre_order())      
print(test_tree.in_order())      
print(test_tree.post_order())      
print(test_tree.contains(15))
print(test_tree.contains(13))
print(test_tree.find_max_val())