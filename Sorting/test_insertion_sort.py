from insertion_sort import insertion_sort

def test_insertion_sort_correct():
  assert insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_insertion_sort_empty():
  assert insertion_sort([]) == []

def test_insertion_sort_singleton():
  assert insertion_sort([5]) == [5]

def test_insertion_sort_contains_negatives():
  assert insertion_sort([5, -2, -1234, 45, -1]) == [-1234, -2, -1, 5, 45]