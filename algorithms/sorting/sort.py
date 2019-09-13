from abc import ABC, abstractmethod

class Sort(ABC):
	
	@abstractmethod
	def sort(unsorted): pass

	'''Takes in a list and two integer indeces and swaps the two elements in place'''
	@staticmethod
	def swap(list, i1, i2):
	  temp = list[i1]
	  list[i1] = list[i2]
	  list[i2] = temp
