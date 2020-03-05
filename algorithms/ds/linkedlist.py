class Node:
  def __init__(self, val: int):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self, head: Node):
    self.head = head
    self.end = head
    self.size = 0 if not head else 1

  def __str__(self):
    repr = ''
    currentNode = self.head
    if currentNode:
      repr += str(currentNode.val)
      currentNode = currentNode.next
    else:
      return repr
    
    while(currentNode):
      repr += '->' + str(currentNode.val)
      currentNode = currentNode.next

    return repr

  def append(self, val: int) -> Node:
    if val:
      if not self.head:
        head = Node(val)
        self.head = head
        self.end = head
        return head
      
      node = Node(val)
      self.end.next = node
      self.end = node
      self.size += 1
      return node

    return None

  def prepend(self, val: int) -> Node:
    if val:
      node = Node(val)
      node.next = self.head
      self.head = node
      self.size += 1
      return node

    return None

  def insert(self, index: int, val: int) -> Node:
    if val and (not self.head or 0 <= index <= self.size):
      if index == 0:
        return self.prepend(val)
      
      node = Node(val)
      currentNode = self.head
      count = 1
      while(count < index):
        currentNode = currentNode.next
        count += 1

      node.next = currentNode.next
      currentNode.next = node
      self.size += 1
      return node

    return None

  def pop(self, index = None) -> Node:
    if index is None:
      index = self.size - 1
    if 0 <= index < self.size:
      if index == 0:
        oldHead = self.head
        self.head = self.head.next
        oldHead.next = None
        self.size -= 1
        return oldHead

      currentNode = self.head
      prevNode = None
      count = 1
      while(count <= index):
        prevNode = currentNode
        currentNode = currentNode.next
        count += 1

      prevNode.next = currentNode.next
      currentNode.next = None
      if not prevNode.next:
        self.end = prevNode

      self.size -= 1
      return currentNode

    return None

  def remove(self, val: int) -> Node:
    currentNode = self.head
    index = 0
    while(currentNode):
      if currentNode.val == val:
        return self.pop(index)
      
      currentNode = currentNode.next
      index += 1

    return None

  def search(self, val: int) -> Node:
    currentNode = self.head
    while(currentNode):
      if currentNode.val == val:
        return currentNode
      currentNode = currentNode.next
    
    return None

if __name__ == '__main__':
  head = Node(5)
  linked = LinkedList(head)
  linked.append(6)
  linked.insert(2, 7)
  print(linked)
