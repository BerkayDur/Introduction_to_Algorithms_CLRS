# pylint: skip-file
from selection_sort import selection_sort

def test_selection_sort_correct_ascending():
  assert selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ascending=True) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_selection_sort_empty_ascending():
  assert selection_sort([], ascending=True) == []

def test_selection_sort_singleton_ascending():
  assert selection_sort([5], ascending=True) == [5]

def test_selection_sort_contains_negatives_ascending():
  assert selection_sort([5, -2, -1234, 45, -1], ascending=True) == [-1234, -2, -1, 5, 45]


def test_selection_sort_correct_descending():
  assert selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ascending=False) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_selection_sort_empty_descending():
  assert selection_sort([], ascending=False) == []

def test_selection_sort_singleton_descending():
  assert selection_sort([5], ascending=False) == [5]

def test_selection_sort_contains_negatives_descending():
  assert selection_sort([5, -2, -1234, 45, -1], ascending=False) == [45, 5, -1, -2, -1234]