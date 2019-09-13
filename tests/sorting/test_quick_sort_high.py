import unittest

from context import algorithms
from test_sort import TestSort
from algorithms.sorting.quicksort_high import QuickSortHigh

class TestQuickSortHigh(unittest.TestCase, TestSort):
	sort_object = QuickSortHigh

if __name__ == '__main__':
	unittest.main()