"""Source code for insertion sourt algorithm: Chapter 2.1"""

def insertion_sort(input_list: list) -> list:
  """
  Sorts the input_list using the insertion sort method - which sorts the list in-place
  
  """
  for i, key in enumerate(input_list[1:], 1):
    j = i-1
    while j >= 0 and input_list[j] > key:
      input_list[j+1] = input_list[j]
      j -= 1
    input_list[j+1] = key
  return input_list

if __name__ == "__main__":
  
  print(insertion_sort([-23,6345,2234,-232,90, 324]))