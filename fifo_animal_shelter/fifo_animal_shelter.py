class Node:
  def __init__(self, value, next = None):
      self.value = value
      self.next = next

class AnimalShelter:
  def __init__(self):
      self.shelter = None
  
  def enqueue(self, animal):
    animal = animal.lower()
    if animal != 'dog' and animal != 'cat': return "Only dogs and cats, please."
    node = Node(animal)
    if not self.shelter: self.shelter = node
    else:
      curr_node = self.shelter
      while curr_node.next:
        curr_node = curr_node.next
      curr_node.next = node
    return self.shelter

  def dequeue(self, pref):
    pref = pref.lower()
    if not self.shelter: return "We currently don't have any pets for adoption"
    if pref == 'dog' or pref == 'cat':
      curr_node = self.shelter
      while curr_node.next is not None:
        if curr_node.value == pref:
          curr_node.value = curr_node.next.value
          curr_node.next = curr_node.next.next
          return pref
        prev = curr_node
        curr_node = curr_node.next
      if curr_node.value == pref:
        prev.next = None
        return pref
      unavailable = 'Sorry, we are all out of ' + pref + 's.'
      return unavailable
    else: return None

  def __str__(self):
        queue = str()
        curr_node = self.shelter
        if not curr_node: return 'None'
        while curr_node.next:
            queue += str(curr_node.value) + ' -> '
            curr_node = curr_node.next
        queue += str(curr_node.value) + ' -> None'
        return queue

cool_pets = AnimalShelter()
print(cool_pets.dequeue('dog'))
cool_pets.enqueue('dog')
print(cool_pets.dequeue('snake'))
print(cool_pets.dequeue('cat'))
cool_pets.enqueue('cat')
cool_pets.enqueue('cat')
cool_pets.enqueue('cat')
cool_pets.enqueue('dog')
print(cool_pets)
print(cool_pets.dequeue('dog'))
print(cool_pets.dequeue('dog'))
print(cool_pets)
