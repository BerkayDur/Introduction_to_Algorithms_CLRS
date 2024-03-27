# pylint: skip-file

from set_sum_to_int import set_sum_to_int

def test_set_sum_to_int_6():
  assert set_sum_to_int([8, 3, 2, 4, 8, 4, 2], 6) == True

def test_set_sum_to_int_8():
  assert set_sum_to_int([8, 3, 2, 4, 8, 4, 2], 8) == True

def test_set_sum_to_int_false_i():
  assert set_sum_to_int([1, 1, 1, 1, 1], 5) == False

def test_set_sum_to_int_false_ii():
  assert set_sum_to_int([13, 8, 3, 2, 10, 234], 9) == False