class Node:
  def __init__(self, val):
      self.val = val
      self.next = None

class Stack:
  def __init__(self):
    self.top = None
  
  def push(self, val):
    node = Node(val)
    node.next = self.top
    self.top = node
  
  def pop(self):
    if not self.top: return "Nothing here"
    removed = self.top.val
    self.top = self.top.next
    return removed

  def peek(self):
    if not self.top: return "I see nothing"
    return self.top.val

  def is_empty(self):
    if self.top: return False
    else: return True

  def __str__(self):
        stack = str()
        curr_node = self.top
        if not curr_node: return 'None'
        while curr_node.next:
            stack += str(curr_node.val) + ' -> '
            curr_node = curr_node.next
        stack += str(curr_node.val) + ' -> None'
        return stack

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

  def peek(self):
    if not self.front: return "I see nothing"
    return self.front.val

  def is_empty(self):
    if self.front: return False
    else: return True

class PseudoQueue(Stack):
  def __init__(self):
      super().__init__()
      self.top = None

  def enqueue(self, val):
    first_stack = PseudoQueue()
    second_stack = PseudoQueue()
    if not self.top:
        second_stack.push(val)
    else:
      curr_node = self.top
      print(self)
      while curr_node.next:
        first_stack.push(curr_node.val)
        curr_node = curr_node.next
      first_stack.push(curr_node.val)
      first_stack.push(val)
      print(first_stack)
      other_node = first_stack.top
      while other_node.next:
        second_stack.push(other_node.val)
        other_node = other_node.next
      second_stack.push(other_node.val)
    self.top = second_stack.top
    return self.top
  
  def dequeue(self):
    return self.pop()

def __str__(self):
    pass

print("Testing Stack Class & Methods")
test_stack = Stack()
print(test_stack.pop())
print(test_stack.peek())
print(test_stack.is_empty())
test_stack.push(3)
test_stack.push(2)
test_stack.push(1)
print(test_stack.pop())
print(test_stack.peek())
print(test_stack.is_empty())
print(test_stack.pop())
print(test_stack.pop())
print("")
print("Testing Queue Class & Methods")
test_queue = Queue()
print(test_queue.dequeue())
print(test_queue.peek())
print(test_queue.is_empty())
test_queue.enqueue(3)
test_queue.enqueue(2)
test_queue.enqueue(1)
print(test_queue.dequeue())
print(test_queue.peek())
print(test_queue.is_empty())
print(test_queue.dequeue())
print(test_queue.dequeue())
print("")
print("Testing PseudoQueue Class & Methods")
test_queue = PseudoQueue()
print(test_queue.dequeue())
print(test_queue.peek())
print(test_queue.is_empty())
test_queue.enqueue(3)
test_queue.enqueue(2)
test_queue.enqueue(1)
print(test_queue.dequeue())
print(test_queue.peek())
print(test_queue.is_empty())
print(test_queue.dequeue())
print(test_queue.dequeue())