# pylint: skip-file
from merge_sort import merge, merge_sort

def test_merge_2_elem_asc():
  lst = [7, 3]
  assert merge(lst, 0, 1, 2, ascending=True) == [3, 7]

def test_merge_larger_lst_asc():
  lst = [3, 26, 41, 52, 9, 38, 49, 57]
  assert merge(lst, 0, 4, 8, ascending=True) == [3, 9, 26, 38, 41, 49, 52, 57]

def test_merge_already_sorted_list_asc():
  lst = list(range(100))
  assert merge(lst, 0, 50, 100, ascending=True) == list(range(100))

def test_merge_2_elem_desc():
  lst = [7, 3]
  assert merge(lst, 0, 1, 2, ascending=False) == [3, 7][::-1]

def test_merge_larger_lst_desc():
  lst = [52, 41, 26, 3, 57, 49, 38, 9]
  assert merge(lst, 0, 4, 8, ascending=False) == [3, 9, 26, 38, 41, 49, 52, 57][::-1]

def test_merge_already_sorted_list_desc():
  lst = list(range(50))[::-1] + list(range(50, 100))[::-1]
  assert merge(lst, 0, 50, 100, ascending=False) == list(range(100))[::-1]


def test_merge_sort_correct_ascending():
  assert merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ascending=True) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_merge_sort_empty_ascending():
  assert merge_sort([], ascending=True) == []

def test_merge_sort_singleton_ascending():
  assert merge_sort([5], ascending=True) == [5]

def test_merge_sort_contains_negatives_ascending():
  assert merge_sort([5, -2, -1234, 45, -1], ascending=True) == [-1234, -2, -1, 5, 45]


def test_merge_sort_correct_descending():
  assert merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ascending=False) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_merge_sort_empty_descending():
  assert merge_sort([], ascending=False) == []

def test_merge_sort_singleton_descending():
  assert merge_sort([5], ascending=False) == [5]

def test_merge_sort_contains_negatives_descending():
  assert merge_sort([5, -2, -1234, 45, -1], ascending=False) == [45, 5, -1, -2, -1234]