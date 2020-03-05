class Stack:
  def __init__(self):
    self.elements = [];

  def __str__(self):
    return '';

  def push(self, el):
    return self.elements.append(el);

  def pop(self):
    return self.elements.pop();

  def peek(self):
    return self.elements[len(self.elements)-1];

  def isEmpty(self) -> bool:
    return len(self.elements) == 0;