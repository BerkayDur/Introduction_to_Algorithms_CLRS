'''Source code for function that computes whether the 
sum of any 2 elements of an array sum to a given number (2.3-8)'''

from helpers import merge_sort

def set_sum_to_int(array_to_search: list[int], sums_to: int) -> bool:
  '''Determines is the sum of 2 elements sum to, sums_to'''
  array_to_search_sorted = merge_sort(array_to_sort=list(array_to_search), ascending=True)

  start_index = 0
  end_index = len(array_to_search) - 1

  while start_index < end_index:
    smn = array_to_search_sorted[start_index] + array_to_search_sorted[end_index]
    if smn == sums_to:
      return True
    if smn < sums_to:
      start_index += 1
    else:
      end_index -= 1
  return False

if __name__ == '__main__':
  print(set_sum_to_int([8, 3, 2, 4, 8, 4, 2], 6))
