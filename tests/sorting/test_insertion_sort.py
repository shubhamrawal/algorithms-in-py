import unittest

from context import algorithms
from test_sort import TestSort
from algorithms.sorting.insertionsort import InsertionSort

class TestInsertionSort(unittest.TestCase, TestSort):
	sort_object = InsertionSort

if __name__ == '__main__':
	unittest.main()