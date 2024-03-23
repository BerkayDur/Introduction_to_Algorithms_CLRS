# pylint: skip-file
from linear_search import linear_search

def test_linear_search_sorted():
  assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == 3

def test_linear_search_shuffled():
  assert linear_search([-2349, 34902, 3, 123, 11239, -212, 904, 243], 243) == 7

def test_linear_search_not_in_sorted():
  assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == -1

def test_linear_search_not_in_shuffled():
  assert linear_search([-2349, 34902, 3, 123, 11239, -212, 904, 243], 345) == -1

def test_linear_search_float_sorted():
  assert linear_search([0.00345, 1/3 - 1/4, 11], 1/12) == 1

def test_linear_search_float_shuffled():
  assert linear_search([-2349.0234, 34902.238492, 3/8, 123/11, 11239, -212.003403, 904.920, 2432.302], 34902.238492) == 1

def test_linear_search_float_not_in_sorted():
  assert linear_search([0.00345, 1/3 - 1/4, 11], 1/15) == -1

def test_linear_search_float_not_in_shuffled():
  assert linear_search([-2349.0234, 34902.238492, 3/8, 123/11, 11239, -212.003403, 904.920, 2432.302], 23534) == -1