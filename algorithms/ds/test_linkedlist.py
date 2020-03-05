import unittest
from linkedlist import LinkedList, Node

class TestLinkedList(unittest.TestCase):
  def test_empty(self):
    linked = LinkedList(None)
    self.assertEqual(str(linked), '', 'should be empty')

  def test_one(self):
    head = Node(5)
    linked = LinkedList(head)
    self.assertEqual(str(linked), '5', 'should be 5')

  def test_append_one(self):
    linked = LinkedList(None)
    linked.append(5)
    self.assertEqual(str(linked), '5', 'should be 5')
    
  def test_append_two(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.append(7)
    self.assertEqual(str(linked), '5->7', 'should be 5->7')

  def test_append_many(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.append(7)
    linked.append(9)
    linked.append(11)
    self.assertEqual(str(linked), '5->7->9->11', 'should be 5->7->9->11')

  def test_prepend_one(self):
    linked = LinkedList(None)
    linked.prepend(5)
    self.assertEqual(str(linked), '5', 'should be 5')
    
  def test_prepend_two(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.prepend(7)
    self.assertEqual(str(linked), '7->5', 'should be 7->5')

  def test_prepend_many(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.prepend(7)
    linked.prepend(9)
    linked.prepend(11)
    self.assertEqual(str(linked), '11->9->7->5', 'should be 11->9->7->5')

  def test_insert_empty(self):
    linked = LinkedList(None)
    linked.insert(0, 5)
    self.assertEqual(str(linked), '5', 'should be 5')

  def test_insert_start(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.insert(0, 2)
    self.assertEqual(str(linked), '2->5', 'should be 2->5')

  def test_insert_at_one(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.append(7)
    linked.insert(1, 6)
    self.assertEqual(str(linked), '5->6->7', 'should be 5->6->7')

  def test_insert_end(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.insert(1, 7)
    self.assertEqual(str(linked), '5->7', 'should be 5->7')

  def test_pop_empty(self):
    linked = LinkedList(None)
    node = linked.pop()
    self.assertEqual(node, None, 'should be None')

  def test_pop_one(self):
    head = Node(5)
    linked = LinkedList(head)
    node = linked.pop()
    self.assertEqual(node.val, 5, 'should be 5')
    self.assertEqual(str(linked), '', 'should be empty')

  def test_pop_two(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.append(7)
    node = linked.pop()
    self.assertEqual(node.val, 7, 'should be 7')
    node = linked.pop()
    self.assertEqual(node.val, 5, 'should be 5')
    self.assertEqual(str(linked), '', 'should be empty')

  def test_remove_empty(self):
    linked = LinkedList(None)
    node = linked.remove(5)
    self.assertEqual(node, None, 'should be None')

  def test_remove_one(self):
    head = Node(5)
    linked = LinkedList(head)
    node = linked.remove(5)
    self.assertEqual(node.val, 5, 'should be 5')
    self.assertEqual(str(linked), '', 'should be empty')

  def test_remove_not_exisiting(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.append(9)
    node = linked.remove(7)
    self.assertEqual(node, None, 'should be None')
    self.assertEqual(str(linked), '5->9', 'should be 5->9')

  def test_search_existing(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.append(7)
    linked.append(11)
    node = linked.search(11)
    self.assertEqual(node.val, 11, 'should be 11')
    self.assertEqual(str(linked), '5->7->11', 'should be 5->7->11')

  def test_search_not_existing(self):
    head = Node(5)
    linked = LinkedList(head)
    linked.append(7)
    linked.append(11)
    node = linked.search(15)
    self.assertEqual(node, None, 'should be None')
    self.assertEqual(str(linked), '5->7->11', 'should be 5->7->11')

if __name__ == '__main__':
  unittest.main()
