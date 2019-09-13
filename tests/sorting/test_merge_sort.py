import unittest

from context import algorithms
from test_sort import TestSort
from algorithms.sorting.mergesort import MergeSort

class TestInsertionSort(unittest.TestCase, TestSort):
	sort_object = MergeSort

if __name__ == '__main__':
	unittest.main()