# pylint: skip-file


from binary_add import binary_add, remove_zeros_from_end


def test_remove_zeros_from_end_correct():
  assert remove_zeros_from_end([0, 0, 0]) == [0]


def test_remove_zeros_from_end_empty():
  assert remove_zeros_from_end([]) == []

def test_remove_zeros_from_end_10000():
  assert remove_zeros_from_end([1, 0, 0, 0, 0]) == [1]

def test_remove_zeros_from_end_000001():
  assert remove_zeros_from_end([0, 0, 0, 0, 0, 1]) == [0, 0, 0, 0, 0, 1]

def test_binary_add_zeros():
  assert binary_add([0], [0, 0, 0, 0]) == [0]

def test_binary_add_one_zero():
  assert binary_add([0, 0, 0, 1], [0]) == [1]


def test_binary_add_16_3():
  assert binary_add([1, 0, 0, 0, 0], [0, 1, 1]) == [1, 0, 0, 1, 1]


def test_binary_add_3_3():
  assert binary_add([1, 1], [1, 1]) == [1, 1, 0]

