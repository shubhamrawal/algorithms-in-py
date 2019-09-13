from algorithms.sorting.quicksort import QuickSort

class QuickSortMedian3(QuickSort):

	'''
	'''
	@staticmethod
	def _partition(unsorted, low, high):
		mid = (low + high)//2
		if unsorted[low] > unsorted[high]:
			QuickSortMedian3.swap(unsorted, low, high)
		if unsorted[mid] > unsorted[high]:
			QuickSortMedian3.swap(unsorted, mid, high)

		pivot_index = mid
		pivot = unsorted[pivot_index]

		left_index = low

		for i in range(low, high-1):
			if unsorted[i] < pivot:
				QuickSortMedian3.swap(unsorted, i, left_index)
				left_index += 1

		QuickSortMedian3.swap(unsorted, left_index, pivot_index)

		return left_index