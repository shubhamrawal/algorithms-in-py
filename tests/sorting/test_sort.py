class TestSort():

	sort_object = None

	def test_empty(self):
		unsorted_list = []
		sorted_list = self.sort_object.sort(unsorted_list)
		self.assertEqual(sorted_list, sorted(unsorted_list))

	def test_one(self):
		unsorted_list = [1]
		sorted_list = self.sort_object.sort(unsorted_list)
		self.assertEqual(sorted_list, sorted(unsorted_list))

	def test_two(self):
		unsorted_list = [10, 2]
		sorted_list = self.sort_object.sort(unsorted_list)
		self.assertEqual(sorted_list, sorted(unsorted_list))

	def test_two_same(self):
		unsorted_list = [10, 10]
		sorted_list = self.sort_object.sort(unsorted_list)
		self.assertEqual(sorted_list, sorted(unsorted_list))

	def test_many(self):
		unsorted_list = [1, 2, 5, 3, 5, 6, 7, 3, 22, 345, 2]
		sorted_list = self.sort_object.sort(unsorted_list)
		self.assertEqual(sorted_list, sorted(unsorted_list))
