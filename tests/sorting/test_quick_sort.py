import unittest

from context import algorithms
from test_sort import TestSort
from algorithms.sorting.quicksort import QuickSort

class TestQuickSort(unittest.TestCase, TestSort):
	sort_object = QuickSort

if __name__ == '__main__':
	unittest.main()