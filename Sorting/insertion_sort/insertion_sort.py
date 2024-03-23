"""Source code for insertion sourt algorithm: Chapter 2.1"""

## Helper(s)
def greater_than(a, b):
  """Functional way of computing greater than"""
  return a > b

def less_than(a, b):
  """Functional way of computing less than"""
  return a < b

def insertion_sort(input_list: list, *, ascending: bool = True) -> list:
  """
  Sorts the input_list using the insertion sort method - which sorts the list in-place
  """
  compare_function = greater_than if ascending else less_than

  for i, key in enumerate(input_list[1:], 1):
    j = i-1
    while j >= 0 and compare_function(input_list[j], key):
      input_list[j+1] = input_list[j]
      j -= 1
    input_list[j+1] = key
  return input_list

if __name__ == "__main__":
  print(insertion_sort([-23,6345,2234,-232,90, 324], ascending=True))
