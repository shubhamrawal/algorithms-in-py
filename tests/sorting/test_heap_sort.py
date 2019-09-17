import unittest

from context import algorithms
from test_sort import TestSort
from algorithms.sorting.heapsort import HeapSort

class TestInsertionSort(unittest.TestCase, TestSort):
	sort_object = HeapSort

if __name__ == '__main__':
	unittest.main()