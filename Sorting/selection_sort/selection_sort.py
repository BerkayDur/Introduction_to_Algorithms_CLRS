"""Source code for the Selection Sort Algorithm CLRS: 2.2-2"""

## Helper(s)
def greater_than(a: int | float, b: int | float) -> bool:
  """Functional way of computing greater than"""
  return a > b

def less_than(a: int | float, b: int | float) -> bool:
  """Functional way of computing less than"""
  return a < b

def selection_sort(input_list: list[int | float], *, ascending: bool = True) -> list[int | float]:
  """ sort a list of numbers using the selection_sort procedure
  """
  compare_function = greater_than if ascending else less_than

  for i in range(len(input_list)-1):
    boundary_term = input_list[i]
    boundary_index = i
    for j in range(i+1, len(input_list)):
      if compare_function(boundary_term, input_list[j]):
        boundary_term = input_list[j]
        boundary_index = j
    input_list[boundary_index] = input_list[i]
    input_list[i] = boundary_term
  return input_list

if __name__ == "__main__":
  print(selection_sort([-23,6345,2234,-232,90, 324], True))