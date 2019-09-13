import unittest

from context import algorithms
from test_sort import TestSort
from algorithms.sorting.bubblesort import BubbleSort

class TestBubbleSort(unittest.TestCase, TestSort):
	sort_object = BubbleSort

if __name__ == '__main__':
	unittest.main()
