
def zero_init_matrix(height:int, width:int) -> list[int]:
  return [[0 for j in range(width)] for i in range(height)]


def matrix_multiply_naive(A:list[int], B:list[int]) -> list[int]:
  n = len(A)
  C = zero_init_matrix(n, n)

  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] = C[i][j] + A[i][k] * B[k][j]
  
  return C

# def _recursive_part(A, B, C, lower, upper)

# def matrix_mulitply_recursive(A: list[int], B: list[int], C:list[int], n):
