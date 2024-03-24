# pylint: skip-file

from binary_add import binary_add, binary_add_var_len

def test_binary_add_zeros():
  assert binary_add([0], [0]) == [0, 0]

def test_binary_add_one_zero():
  assert binary_add([1], [0]) == [0, 1]

def test_binary_add_16_3():
  assert binary_add([1, 0, 0, 0, 0], [0, 0, 0, 1, 1]) == [0, 1, 0, 0, 1, 1]

def test_binary_add_3_3():
  assert binary_add([1, 1], [1, 1]) == [1, 1, 0]


def test_binary_add_var_len_zeros():
  assert binary_add_var_len([0], [0]) == [0]

def test_binary_add_var_len_one_zero():
  assert binary_add_var_len([1], [0]) == [1]

def test_binary_add_var_len_16_3():
  assert binary_add_var_len([1, 0, 0, 0, 0], [1, 1]) == [1, 0, 0, 1, 1]

def test_binary_add_var_len_3_3():
  assert binary_add_var_len([1, 1], [1, 1]) == [1, 1, 0]