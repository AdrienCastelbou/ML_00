from lib2to3.pytree import Base
from typing import Any
from matrix import Matrix

def print_matrix(matrix):
    print(matrix.shape)
    for r in matrix.data:
        print(r)

if __name__ == "__main__":
#    matrix1 = Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])
#    print_matrix(matrix1)
#    matrix2 = Matrix((2, 3))
#    print_matrix(matrix2)
#    matrix2 = Matrix([[10, 12, 11], [3.0, 4.5, 89]])
#    print_matrix(matrix1 + matrix2)
#    try:
#        print_matrix(1 + matrix1)
#    except Exception as err:
#        print(f"Error occured: {err}")
#    print_matrix(matrix2 - matrix1)
    matrix1 = Matrix([[1, 2, 0], [4, 3, -1]])
    matrix2 = Matrix([[5, 1], [2, 3], [3, 4]])
    #print_matrix(matrix1)
    #print_matrix(matrix2)
    print_matrix(matrix1 * matrix2)
    print_matrix(matrix1 * matrix2)

    print_matrix(3 * matrix1)

    m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
    [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0],
    [2.0, 3.0],
    [4.0, 5.0],
    [6.0, 7.0]])
    print(m1 * m2)
    print("---")
    print(m1)
    print("---")
    print(Matrix([[1, 2, 5], [2, 4, 6]]).T())
