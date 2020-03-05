class Node:
  def __init__(self, val: int):
    self.val = val;
    self.next = None;

class LinkedList:
  def __init__(self, head: Node):
    self.head = head;
    self.end = head;
    self.size = 0 if not head else 1;

  def __str__(self):
    repr = '';
    currentNode = self.head;
    if currentNode:
      repr += str(currentNode.val);
      currentNode = currentNode.next;
    else:
      return repr;
    
    while(currentNode):
      repr += '->' + str(currentNode.val);
      currentNode = currentNode.next;

    return repr;

  def append(self, val: int) -> Node:
    if val:
      node = Node(val);
      self.end.next = node;
      self.end = node;
      self.size += 1;
      return node;

    return None;

  def prepend(self, val: int) -> Node:
    if val:
      node = Node(val);
      node.next = self.head;
      self.head = node;
      self.size += 1;
      return node;

    return None;

  def insert(self, index: int, val: int) -> Node:
    if val and index < self.size:
      if index == 0:
        return self.prepend(val);
      else:
        node = Node(val);
        currentNode = self.head;
        count = 1;
        while(count < index):
          currentNode = currentNode.next;
          count += 1;

        node.next = currentNode.next;
        currentNode.next = node;
        self.size += 1;
        return node;

    return None;

if __name__ == '__main__':
  head = Node(5);
  linked = LinkedList(head);
  print(linked);
  linked.append(7);
  print(linked);
  linked.prepend(1);
  print(linked);
  linked.insert(1, 3);
  print(linked);
