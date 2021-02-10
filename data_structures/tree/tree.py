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

def fizz_buzz_tree(tree):
  fizzbuzz_tree = BinaryTree()
  if not tree.root: return fizzbuzz_tree
  fizzbuzz_tree.root = happy_fizzbuzz_tree_helper(tree.root)
  return fizzbuzz_tree

def happy_fizzbuzz_tree_helper(node):
    if not node: return None
    fizz_val = fizzify(node.val)
    fizz_node = Node(fizz_val)
    fizz_node.left = happy_fizzbuzz_tree_helper(node.left)
    fizz_node.right = happy_fizzbuzz_tree_helper(node.right)
    return fizz_node

def fizzify(val):
  if val % 15 == 0: val = "fizzbuzz"
  elif val % 3 == 0: val = "fizz"
  elif val % 5 == 0: val = "buzz"
  else: val = str(val)
  return (val)

def sum_odd_tree(tree):
  if not tree.root: return 0
  tree_sum = odd_tree_helper(tree.root)
  return tree_sum

def odd_tree_helper(node):
  tree_sum = 0
  if not node: return tree_sum
  if node.val % 2 == 1: tree_sum += node.val
  tree_sum += odd_tree_helper(node.left)
  tree_sum += odd_tree_helper(node.right)
  return tree_sum

test_tree = BinarySearchTree()
test_tree.add(10)
test_tree.add(5)
test_tree.add(14)
test_tree.add(15)
test_tree.add(3)
test_tree.add(9)
print(test_tree)
print(test_tree.pre_order())      
print(test_tree.in_order())      
print(test_tree.post_order())      
print(test_tree.contains(15))
print(test_tree.contains(13))
print(test_tree.find_max_val())

test_tree2 = BinarySearchTree()
test_tree2.root = Node(2)
test_tree2.root.left = Node(7)
test_tree2.root.left.left = Node(2)
test_tree2.root.left.right = Node(6)
test_tree2.root.left.right.left = Node(5)
test_tree2.root.left.right.right = Node(11)
test_tree2.root.right = Node(5)
test_tree2.root.right.right = Node(9)
test_tree2.root.right.right.left = Node(4)
print(test_tree2.breadth_first())

print(fizz_buzz_tree(test_tree))
print(sum_odd_tree(test_tree2))
print(sum_odd_tree(test_tree))