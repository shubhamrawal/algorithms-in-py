import math
from algorithms.sorting.sort import Sort

class HeapSort(Sort):

	'''
	'''
	@staticmethod
	def sort(unsorted):
		if len(unsorted) < 2:
			return unsorted

		temp = unsorted.copy()
		sorted_list = []

		HeapSort._build_max_heap(temp)
		for i in range(len(temp), 0, -1):
			HeapSort.swap(temp, 0, len(temp)-1)
			sorted_list.insert(0, temp.pop())
			HeapSort._max_heapify(temp, 0)

		return sorted_list

	@staticmethod
	def _build_max_heap(unsorted):
		heap_size = len(unsorted)
		for i in range(math.ceil(heap_size/2), -1, -1):
			HeapSort._max_heapify(unsorted, i)

	@staticmethod
	def _max_heapify(heap, i):
		left = HeapSort._get_left(i)
		right = HeapSort._get_right(i)
		heap_size = len(heap)

		largest = left if left < heap_size and heap[left] > heap[i] else i

		if right < heap_size and heap[right] > heap[largest]:
			largest = right

		if not largest == i:
			HeapSort.swap(heap, i, largest)
			HeapSort._max_heapify(heap, largest)

	@staticmethod
	def _get_left(i):
		return 2*i + 1

	@staticmethod
	def _get_right(i):
		return 2*i + 2

	@staticmethod
	def _get_parent(i):
		return (i-1)//2
