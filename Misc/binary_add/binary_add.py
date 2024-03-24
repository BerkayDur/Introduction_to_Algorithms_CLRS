"""Source code for binary add 2.1-5 CLRS"""

# Helper(s)
def remove_zeros_from_end(binary_array: list[int]) -> list[int]:
  """Removes extra zeros from the end of a list of numbers.
  
  Generally used in the context of a reversed binary array to truncate."""
  while len(binary_array) > 1 and binary_array[-1] == 0:
    binary_array.pop()
  return binary_array

def binary_add(binary_array_1: list[int], binary_array_2: list[int]) -> list[int]:
  """binary add variable length arrays"""
  sum_binary_arrays_rev = [0]
  arr1_count = len(binary_array_1) - 1
  arr2_count = len(binary_array_2) - 1
  sum_array_counter = 0
  while True:
    if arr1_count < 0 and arr2_count < 0:
      sum_binary_arrays_rev = remove_zeros_from_end(sum_binary_arrays_rev)
      sum_binary_arrays_rev.reverse()
      return sum_binary_arrays_rev
    sum_binary_arrays_rev.append(0)
    if arr1_count >= 0:
      sum_binary_arrays_rev[sum_array_counter] += binary_array_1[arr1_count]
      arr1_count -= 1
    if arr2_count >= 0:
      sum_binary_arrays_rev[sum_array_counter] += binary_array_2[arr2_count]
      arr2_count -= 1
    sum_binary_arrays_rev[sum_array_counter+1] += sum_binary_arrays_rev[sum_array_counter] // 2
    sum_binary_arrays_rev[sum_array_counter] %= 2
    sum_array_counter += 1

if __name__ == "__main__":
  print(binary_add([0], [0]))