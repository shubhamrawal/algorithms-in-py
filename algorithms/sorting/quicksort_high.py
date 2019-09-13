from algorithms.sorting.quicksort import QuickSort

class QuickSortHigh(QuickSort):

	'''

	'''
	@staticmethod
	def _partition(unsorted, low, high):
		pivot_index = high-1
		pivot = unsorted[pivot_index]

		left_index = low

		for i in range(low, high-2):
			if unsorted[i] < pivot:
				QuickSortHigh.swap(unsorted, i, left_index)
				left_index += 1

		QuickSortHigh.swap(unsorted, left_index, pivot_index)

		return left_index
