import pytest
from matrix_multiply import matrix_multiply_naive

def test_matrix_mulitply_naive_identity():
  assert matrix_multiply_naive([[1,0],[0,1]], [[3,4],[15,22]]) == [[3,4],[15,22]]

def test_matrix_mulitply_naive_identity2():
  assert matrix_multiply_naive([[3,4],[15,22]], [[1,0],[0,1]]) == [[3,4],[15,22]]

def test_matrix_mulitply_naive_1():
  assert matrix_multiply_naive([[1,2],[3,4]], [[5,6],[7,8]]) == [[19, 22], [43, 50]]

def test_matrix_mulitply_naive_2():

  matrix1 = [
      [5, 3, 2, 8, 1, 4],
      [7, 9, 6, 2, 5, 3],
      [1, 4, 7, 5, 9, 6],
      [8, 2, 3, 1, 4, 7],
      [6, 5, 9, 3, 8, 2],
      [4, 7, 1, 6, 2, 9]
  ]

  matrix2 = [
      [2, 4, 6, 8, 10, 12],
      [1, 3, 5, 7, 9, 11],
      [15, 14, 13, 12, 11, 10],
      [16, 18, 20, 22, 24, 26],
      [19, 17, 15, 13, 11, 9],
      [25, 23, 21, 19, 17, 15]
  ]

  result = [
    [290, 310, 330, 350, 370, 390],
    [315, 329, 343, 357, 371, 385],
    [512, 495, 478, 461, 444, 427],
    [330, 327, 324, 321, 318, 315],
    [402, 401, 400, 399, 398, 397],
    [389, 400, 411, 422, 433, 444]
  ]

  assert matrix_multiply_naive(matrix1, matrix2) == result