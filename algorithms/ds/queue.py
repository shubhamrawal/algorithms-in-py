class Queue:
  def __init__(self):
    self.elements = [];

  def __str__(self):
    return '';

  def enqueue(self, el):
    return self.elements.append(el);

  def dequeue(self):
    return self.elements.pop(0);