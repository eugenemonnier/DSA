class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return new_node

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node
        self.length += 1
        return self.head

    def array(self):
        val_list = list()
        current = self.head
        while current:
            val_list.append(current.value)
            current = current.next
        return val_list

    def includes(self, val):
        if not self.head: return False
        elif self.head.value == val: return True

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            if curr_node.value == val: return True

        return False

    def insert(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.head

    def insert_before(self, val, new_val):
        self.length += 1
        new_node = Node(new_val)
        curr_node = self.head
        valid_input = False

        while curr_node.next:
            if curr_node.value == val:
                new_node.next = self.head
                self.head = new_node
                valid_input = True
                break
            elif curr_node.next.value == val:
                new_node.next = curr_node.next
                curr_node.next = new_node
                valid_input = True
                break
            curr_node = curr_node.next

        if not valid_input: return 'Search value not found'
        return self.head

    def insert_after(self, val, new_val):
        self.length += 1
        new_node = Node(new_val)
        curr_node = self.head
        valid_input = False

        while curr_node.next:
            if curr_node.value == val:
                new_node.next = curr_node.next
                curr_node.next = new_node
                valid_input = True
                break
            elif (curr_node.next.value == val):
                new_node.next = curr_node.next.next
                curr_node.next.next = new_node
                valid_input = True
                break
            curr_node = curr_node.next

        if not valid_input: return 'Search value not found'
        return self.head

    def kth(self, k):
        k += 1
        curr_node = self.head
        value_list = []

        if (k <= 0): return 'Invalid input value. Input must be greater than -1.'

        while curr_node.next:
            value_list.append(curr_node.value)
            if len(value_list) > k: value_list.pop(0)
            curr_node = curr_node.next

        value_list.append(curr_node.value)
        if len(value_list) > k: value_list.pop(0)

        if len(value_list) < k: return 'Input value is greater than the length of the list.'
        else: return value_list[0]

    def __str__(self):
        linked_string = str()
        curr_node = self.head
        if not curr_node: return 'None'
        while curr_node.next:
            linked_string += str(curr_node.value) + ' -> '
            curr_node = curr_node.next
        linked_string += str(curr_node.value) + ' -> None'
        return linked_string

def merge_lists(list_a, list_b):
    merged_ll = LinkedList()
    curr_node_a = list_a.head
    curr_node_b = list_b.head

    while curr_node_a or curr_node_b:
        if curr_node_a:
            merged_ll.append(curr_node_a.value)
            curr_node_a = curr_node_a.next
        if curr_node_b:
            merged_ll.append(curr_node_b.value)
            curr_node_b = curr_node_b.next
    return merged_ll

class Hashtable():
  def __init__(self, size):
    self.size = size
    self.indicies = [None] * self.size

  def add(self, key, val):
    hashed = self.hash(key)
    if not self.indicies[hashed]: self.indicies[hashed] = LinkedList()
    self.indicies[hashed].append([key, val])

  def contains(self, key):
      hashed_key = self.hash(key)
      if self.indicies[hashed_key]:
          key_list = self.indicies[hashed_key].array()
          for vals in key_list:
              if vals[0] == key: return True
      return False

  def get(self, key):
      if self.contains(key):
          hashed_key = self.hash(key)
          key_list = self.indicies[hashed_key].array()
          for values in key_list:
              if values[0] == key: return(values[1])
      raise ValueError('Key does not exist.')

  def hash(self, key):
      if not isinstance(key, str): key = str(key)
      ascii_val = 1
      for char in key: ascii_val += ord(char)
      hashed_key = ascii_val * 599 % self.size
      return hashed_key

  def __str__(self):
      output = ''
      for index in self.indicies:
          if index: output += ('').join(str(elem) for elem in index.array())
      if not output: return 'None'
      return output

test_table = Hashtable(1024)
test_table.add('hashtable', 20)
print(test_table.get('hashtable'))
print(test_table)