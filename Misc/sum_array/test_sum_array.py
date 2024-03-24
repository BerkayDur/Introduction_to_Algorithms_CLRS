# pylint: skip-file

from sum_array import sum_array

def test_sum_array_pos():
  assert sum_array([5, 3, 1, 534]) == 543

def test_sum_array_neg():
  assert sum_array([-5, -3, -1, -534]) == -543

def test_sum_array_mix():
  assert sum_array([-5, 3, -1, 534]) == 531

def test_sum_array_empty():
  assert sum_array([]) == 0

def test_sum_array_zeros():
  assert sum_array([0, 0, 0, 0]) == 0