import unittest

from context import algorithms
from test_sort import TestSort
from algorithms.sorting.quicksort_median3 import QuickSortMedian3

class TestQuickSortMedian3(unittest.TestCase, TestSort):
	sort_object = QuickSortMedian3

if __name__ == '__main__':
	unittest.main()