"""Source code for binary add 2.1-5 CLRS"""

def binary_add(binary_array_1: list[int], binary_array_2: list[int]) -> list[int]:
  """assume binary_array_1 and binary_array_2 are the same length"""
  output_len = len(binary_array_1) + 1
  sum_binary_arrays = [0] * output_len
  for i in range(output_len-2, -1, -1):
    sum_binary_arrays[i+1] += binary_array_1[i] + binary_array_2[i]
    sum_binary_arrays[i] = sum_binary_arrays[i+1] // 2
    sum_binary_arrays[i+1] %= 2
  return sum_binary_arrays

def binary_add_var_len(binary_array_1: list[int], binary_array_2: list[int]) -> list[int]:
  """binary add variable length arrays"""
  sum_binary_arrays_rev = [0]
  i = len(binary_array_1) - 1
  j = len(binary_array_2) - 1
  k = 0
  while True:
    if i < 0 and j < 0:
      if sum_binary_arrays_rev[-1] == 0:
        sum_binary_arrays_rev.pop()
      sum_binary_arrays_rev.reverse()
      return sum_binary_arrays_rev
    sum_binary_arrays_rev.append(0)
    if i >= 0:
      sum_binary_arrays_rev[k] += binary_array_1[i]
      i -= 1
    if j >= 0:
      sum_binary_arrays_rev[k] += binary_array_2[j]
      j -= 1
    sum_binary_arrays_rev[k+1] += sum_binary_arrays_rev[k] // 2
    sum_binary_arrays_rev[k] %= 2
    k += 1

if __name__ == "__main__":
  print(binary_add_var_len([0], [0]))