# pylint: skip-file
from binary_search import binary_search

def test_binary_search_in1():
  assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == 3

def test_binary_search_in2():
  assert binary_search([-2349, -212, 3, 123, 243, 904, 11239, 34902], 243) == 4

def test_binary_search_not_in1():
  assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == -1

def test_binary_search_not_in2():
  assert binary_search([-2349, -212, 3, 123, 243, 904, 11239, 34902], 345) == -1

def test_binary_search_float_in1():
  assert binary_search([0.00345, 1/3 - 1/4, 11], 1/12) == 1

def test_binary_search_float_in2():
  assert binary_search([-2349.0234, -212.003403, 3/8, 123/11, 904.920, 2432.302, 11239, 34902.238492], 34902.238492) == 7

def test_binary_search_float_not_in1():
  assert binary_search([0.00345, 1/3 - 1/4, 11], 1/15) == -1

def test_binary_search_float_not_in2():
  assert binary_search([-2349.0234, -212.003403, 3/8, 123/11, 904.920, 2432.302, 11239, 34902.238492], 23534) == -1