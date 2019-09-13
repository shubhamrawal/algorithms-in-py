from algorithms.sorting.sort import Sort

class BubbleSort(Sort):

	'''
	Takes an unsorted list and uses bubble sort to return the sorted list

	Compare two elements and swaps them such that the higher element has a higher index
	Keep doing that till the largest element bubbles to the end of the list
	Repeat for the rest of the list till the list is sorted
	'''
	@staticmethod
	def sort(unsorted):
		sorted_list = unsorted.copy()

		for i in range(len(sorted_list)-1, 0, -1):
		  for j in range(i):
		    if(sorted_list[j] > sorted_list[j+1]):
		      BubbleSort.swap(sorted_list, j, j+1)

		return sorted_list