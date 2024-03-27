'''Source code for the binary search algorithm from 2.3-6'''


## Helper(s)
def absolute_diff_compare(a, b, eps=1e-10):
  """Helper that computes equality based on closeness (to account for float-point precision)"""
  return abs(a - b) < eps

def binary_search(list_to_search: list[int | float], search_for: int | float) -> list[int | float]:
  '''Finds the index of a particular value in a sorted array'''
  start = 0
  end = len(list_to_search)
  while start + 1 < end:
    m = (start + end) // 2
    if absolute_diff_compare(list_to_search[m], search_for):
      return m

    if list_to_search[m] < search_for:
      start = m
    else:
      end = m

  return -1


if __name__ == '__main__':
  print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
