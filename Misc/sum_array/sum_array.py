"""Source code of function that sums array 2.1-2"""

def sum_array(array: list[float]) -> float:
  """Sums the elements of an array"""
  smn = 0
  for elem in array:
    smn += elem
  return smn

if __name__ == "__main__":
  print(sum_array([4, 234, -23, 450, -234]))
