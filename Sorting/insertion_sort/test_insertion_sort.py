# pylint: skip-file
from insertion_sort import insertion_sort

def test_insertion_sort_correct_ascending():
  assert insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ascending=True) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_insertion_sort_empty_ascending():
  assert insertion_sort([], ascending=True) == []

def test_insertion_sort_singleton_ascending():
  assert insertion_sort([5], ascending=True) == [5]

def test_insertion_sort_contains_negatives_ascending():
  assert insertion_sort([5, -2, -1234, 45, -1], ascending=True) == [-1234, -2, -1, 5, 45]


def test_insertion_sort_correct_descending():
  assert insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ascending=False) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_insertion_sort_empty_descending():
  assert insertion_sort([], ascending=False) == []

def test_insertion_sort_singleton_descending():
  assert insertion_sort([5], ascending=False) == [5]

def test_insertion_sort_contains_negatives_descending():
  assert insertion_sort([5, -2, -1234, 45, -1], ascending=False) == [45, 5, -1, -2, -1234]