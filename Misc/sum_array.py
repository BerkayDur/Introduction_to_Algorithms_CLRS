"""Source code of function that sums array"""

def sum_array(array: list[float]) -> float:
  smn = 0
  for elem in array:
    smn += elem
  return smn