from algorithms.sorting.sort import Sort

class MergeSort(Sort):

	'''

	'''
	@staticmethod
	def sort(unsorted):
		# base case
		n_elements = len(unsorted)
		if n_elements < 2:
			return unsorted.copy()

		# recursive case
		sorted_left = MergeSort.sort(unsorted[:n_elements//2])
		sorted_right = MergeSort.sort(unsorted[n_elements//2:])

		return MergeSort._merge(sorted_left, sorted_right)

	@staticmethod
	def _merge(left, right):
		merged = []
		left_index = 0
		right_index = 0

		# merge the two lists by comparing the first elements in each sorted list
		# and adding the smallest one to the merged list
		# increment the index of the list from which the element is added and repeat till
		# we get a sorted list
		while(left_index < len(left) and right_index < len(right)):
			if(left[left_index] < right[right_index]):
				merged.append(left[left_index])
				left_index += 1
			else:
				merged.append(right[right_index])
				right_index += 1

		if(left_index == len(left)):
			merged.extend(right[right_index:])

		if(right_index == len(right)):
			merged.extend(left[left_index:])

		return merged



