from algorithms.sorting.sort import Sort

class QuickSort(Sort):

	'''

	'''
	@staticmethod
	def sort(unsorted):
		sorted_list = unsorted.copy()

		if len(sorted_list) < 2:
			return sorted_list

		return QuickSort.quicksort(sorted_list, 0, len(sorted_list))

	'''

	'''
	@staticmethod
	def quicksort(unsorted, low, high):

		if(low < high):
			pivot_index = QuickSort._partition(unsorted, low, high)
			QuickSort.quicksort(unsorted, low, pivot_index)
			QuickSort.quicksort(unsorted, pivot_index + 1, high)

		return unsorted

	'''

	'''
	@staticmethod
	def _partition(unsorted, low, high):
		pivot_index = low
		pivot = unsorted[pivot_index]

		left_index = low+1

		for i in range(low+1, high):
			if unsorted[i] < pivot:
				QuickSort.swap(unsorted, i, left_index)
				left_index += 1

		left_index -= 1
		QuickSort.swap(unsorted, pivot_index, left_index)
		
		return left_index
