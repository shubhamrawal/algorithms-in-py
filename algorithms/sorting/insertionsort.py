from algorithms.sorting.sort import Sort

class InsertionSort(Sort):

	'''
	Takes an unsorted list and uses insertion sort to return the sorted list

	Start from the left and compare an element to all its predecessors till a smaller element is found
	Insert the element in its right place
	Continue till the list is sorted
	'''
	@staticmethod
	def sort(unsorted):
		sorted_list = unsorted.copy()

		for i in range(1, len(sorted_list)):
			for j in range(i, 0, -1):
				if sorted_list[j] >= sorted_list[j-1]:
					break
				
				InsertionSort.swap(sorted_list, j, j-1)
		
		return sorted_list			