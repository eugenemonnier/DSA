class Node:
  def __init__(self, val, next = None):
      self.val = val
      self.next = next
  def __str__(self):
    node_str = "Node: "
    node_str += str(self.val)
    node_str += " -> "
    node_str += str(self.next)
    return node_str

class LinkedList:
  def __init__(self):
      self.head = None
      self.length = 0

  def append(self, val):
    node = Node(val)
    if not self.head: self.head = node
    else:
      curr_node = self.head
      while curr_node.next:
        curr_node = curr_node.next
      curr_node.next = node
      self.length += 1

  def insert_before(self, val, new_val):
    node = Node(new_val)
    curr_node = self.head

    while curr_node.next:
      if curr_node.val == val:
        node.next = self.head
        self.head = node
        self.length += 1
        return self.head
      elif curr_node.next.val == val:
          node.next = curr_node.next
          curr_node.next = node
          self.length += 1
          return self.head
      curr_node = curr_node.next
    return "Input value not found"

  def insert_after(self, val, new_val):
    node = Node(new_val)
    curr_node = self.head

    while curr_node.next:
      if curr_node.val == val:
        self.length += 1
        if curr_node.next:
          node.next = curr_node.next
          curr_node.next = node
          return self.head
        else: 
          curr_node.next = node
          return self.head
      curr_node = curr_node.next
    if curr_node.val == val: 
      self.length += 1
      curr_node.next = node
      return self.head

    return "Input value not found"

  def __str__(self):
      linked_string = str()
      curr_node = self.head
      if not curr_node: return "None"
      while curr_node.next:
        linked_string += str(curr_node.val) + ' -> '
        curr_node = curr_node.next
      linked_string += str(curr_node.val) + ' -> None'
      return linked_string

test_ll = LinkedList()
test_ll.append(1)
test_ll.append(3)
test_ll.append(5)
print(test_ll.insert_before(3,2))
print(test_ll.insert_before(11,12))
print(test_ll.insert_after(3,4))
print(test_ll.insert_after(5,6))
print(test_ll.insert_after(7,8))
print(test_ll)