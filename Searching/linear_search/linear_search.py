"""Source code for linear search algorithms: Chapter 2.1 Exercise 4"""

## Helper(s)
def absolute_diff_compare(a, b, eps=1e-10):
  """Helper that computes equality based on closeness (to account for float-point precision)"""
  return abs(a - b) < eps

def linear_search(array: list[float], search_for: float) -> int:
  """Linear Search algorithms searches for search_for in list, array"""
  for i, key in enumerate(array):
    if absolute_diff_compare(key, search_for):
      return i
  return -1

if __name__ == "__main__":
  print(linear_search([-23.345,6345.38,2234,-232.234, 90, 324], 90))
