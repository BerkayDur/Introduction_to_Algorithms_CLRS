'''Helper for set_sum_to_int, where merge sort is used to keep worst-case running time to n*lg(n)'''

## Helper(s)
def greater_than(a: int | float, b: int | float) -> bool:
  """Functional way of computing greater than"""
  return a > b

def less_than(a: int | float, b: int | float) -> bool:
  """Functional way of computing less than"""
  return a < b

def merge(array_to_sort: list[int | float],
  p: int, q: int, r:int, *, ascending: bool) -> list[int | float]:
  '''Merge procedure combines 2 sorted subarrays within array_to_sort'''

  compare_function = greater_than if ascending else less_than

  left_array = array_to_sort[p:q]
  right_array = array_to_sort[q:r]
  len_l = len(left_array)
  len_r = len(right_array)
  i = 0
  j = 0
  k = p

  while i < len_l and j < len_r:
    if compare_function(right_array[j], left_array[i]):
      array_to_sort[k] = left_array[i]
      i += 1
      k += 1
    else:
      array_to_sort[k] = right_array[j]
      j += 1
      k += 1

  while i < len_l:
    array_to_sort[k] = left_array[i]
    i += 1
    k += 1
  while j < len_r:
    array_to_sort[k] = right_array[j]
    j += 1
    k += 1

  return array_to_sort

def merge_sort(array_to_sort: list[int | float],
  start_index: int = None, final_index: int = None, *,
  ascending: bool = True) -> list[int | float]:
  '''Sorts A in-place (and return it) using the merge-sort procedure'''
  if start_index is None:
    start_index = 0
  if final_index is None:
    final_index = len(array_to_sort)
  if len(array_to_sort) == 0 or start_index + 1 == final_index:
    return array_to_sort
  mid = (start_index + final_index) // 2
  merge_sort(array_to_sort, start_index, mid, ascending=ascending)
  merge_sort(array_to_sort, mid, final_index, ascending=ascending)
  return merge(array_to_sort, start_index, mid, final_index, ascending=ascending)


if __name__ == '__main__':
  print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ascending=True))
