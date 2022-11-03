from matrix import Matrix, Vector


def matrix_creation_test():
    print("<*** Basic Matrix Creation ***>")
    print("- Create a Matrix using data")
    print("Use [[1.0, 13, 11], [3.0, 4.0, 89]]")
    print(f"Output: {Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])}")
    print("- Create a Matrix using shape")
    print("Use (2, 3)")
    print(f"Output: {Matrix((2, 3))}")
    print("- Using Wrong Inputs")
    try:
        Matrix([["1.0", 13, 11], [3.0, 4.0, 89]])
    except Exception as err:
        print(err)
    try:
        Matrix([[1.0, 10, 13, 11], [3.0, 4.0, 89]])
    except Exception as err:
        print(err)
    try:
        Matrix((2))
    except Exception as err:
        print(err)
    try:
        Matrix((0, 1))
    except Exception as err:
        print(err)
    try:
        Matrix((0, "1"))
    except Exception as err:
        print(err)
    print("<*** End of Basics Tests")

def matrix_addition_test():
    print("<*** Addition tests ***>")
    print("- Additions between matrices")
    matrix1 = Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])
    matrix2 = Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])
    print(f"{matrix1} + {matrix2} = {matrix1 + matrix2}")
    matrix2 = Matrix((2, 3))
    print(f"{matrix1} + {matrix2} = {matrix1 + matrix2}")
    matrix1 = Matrix([[11.0, 130, -11], [3.0, 4.0, 89]])
    matrix2 = Matrix([[-331.0, -13, -11], [3.44, 401, 89]])
    print(f"{matrix1} + {matrix2} = {matrix1 + matrix2}")
    print("- Bad inputs")
    try:
        print(f"{matrix1} + {2} = {matrix1 + 2}")
    except Exception as err:
        print(err)
    try:
        print(f"{2} + {matrix2} = {2 + matrix2}")
    except Exception as err:
        print(err)
    try:
        matrix2 = Matrix((2, 4))
        print(f"{matrix1} + {matrix2} = {matrix1 + matrix2}")
    except Exception as err:
        print(err)

def matrix_substraction_test():
    print("<*** Substraction tests ***>")
    print("- Substractions between matrices")
    matrix1 = Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])
    matrix2 = Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])
    print(f"{matrix1} - {matrix2} = {matrix1 - matrix2}")
    matrix2 = Matrix((2, 3))
    print(f"{matrix1} - {matrix2} = {matrix1 - matrix2}")
    matrix1 = Matrix([[11.0, 130, -11], [3.0, 4.0, 89]])
    matrix2 = Matrix([[-331.0, -13, -11], [3.44, 401, 89]])
    print(f"{matrix1} - {matrix2} = {matrix1 - matrix2}")
    print("- Bad inputs")
    try:
        print(f"{matrix1} - {2} = {matrix1 - 2}")
    except Exception as err:
        print(err)
    try:
        print(f"{2} - {matrix2} = {2 - matrix2}")
    except Exception as err:
        print(err)
    try:
        matrix2 = Matrix((2, 4))
        print(f"{matrix1} + {matrix2} = {matrix1 + matrix2}")
    except Exception as err:
        print(err)


def matrix_div_test():
    print("<*** Division test ***>")
    print("- Division by scalar")
    matrix1 = Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])
    print(f"{matrix1} / {3} = {matrix1 / 3}")
    print(f"{matrix1} / {2.5} = {matrix1 / 2.5}")
    print("- Bad Inputs")
    matrix2 = Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])
    try:
        print(f"{matrix1} / {matrix2} = {matrix1 / matrix2}")
    except Exception as err:
        print(err)
    try:
        print(f"{3} / {matrix2} = {3 / matrix2}")
    except Exception as err:
        print(err)


def matrix_mul_test():
    print("<** Multiplication Tests ***>")
    print("Multiplication by Matrix")
    matrix1 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [0.0, 2.0, 4.0, 6.0]])
    matrix2 = Matrix([[0.0, 1.0],
             [2.0, 3.0],
             [4.0, 5.0],
             [6.0, 7.0]])
    print(f"{matrix1} * {matrix2} = {matrix1 * matrix2}")
    matrix1 = Matrix([[1, 2.0, 3.0],
             [4.0, 5.0, 6.0]])
    matrix2 = Matrix([[7.0, 8.0],
             [9.0, -1],
             [-2, -3]])
    print(f"{matrix1} * {matrix2} = {matrix1 * matrix2}") 
    matrix2 = Matrix((3, 2))
    print(f"{matrix1} * {matrix2} = {matrix1 * matrix2}")
    print("- Multiplication by scalar")
    matrix1 = Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])
    print(f"{matrix1} * {3} = {matrix1 * 3}")
    print(f"{2.5} * {matrix1} = {2.5 * matrix1}")
    print("- Multiplication by Vector")
    matrix1 = Matrix([[0.0, 1.0, 2.0],
[0.0, 2.0, 4.0]])
    v1 = Vector([[1], [2], [3]])
    print(f"{matrix1} * {v1} =  {matrix1 * v1}")
    print("- Bad Inputs")
    matrix2 = Matrix([[1.0, 13, 11], [3.0, 4.0, 89]])
    try:
        print(f"{matrix1} * {matrix2} = {matrix1 * matrix2}")
    except Exception as err:
        print(err)
    try:
        v1 = Vector([[1, 2, 3]])
        print(f"{matrix1} * {v1} = {matrix1 * v1}")
    except Exception as err:
        print(err)


def vector_test():
    print("<** Vectors Tests ***>")
    print("- dot product")
    v1 = Vector([[1, 3, -5]])
    v2 = Vector([[4, -2, -1]])
    print(f"{v1} . {v2} = {v1.dot(v2)}")
    print("- Multiplications")
    v1 = Vector([[1], [2], [3]])
    v2 = Vector([[4], [5], [6]])
    print(f"{v1} * {v2} =  {v1 * v2}")
    m1 = Matrix([[1, 2, 3]])
    print(f"{v1} * {v2} =  {v1 * v2}")
    matrix1 = Matrix([[7, 5], [1, 0], [4, 9]])
    v1 = Vector([[1, 3, 0]])
    print(f"{v1} * {matrix1} =  {v1 * matrix1}")
    return

def subject_test():
    m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
    print(m1.shape)
    print(m1.T())
    print(m1.T().shape)
    m1 = Matrix([[0., 2., 4.], [1., 3., 5.]])
    print(m1.shape)
    print(m1.T())
    print(m1.T().shape)
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
    [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0],
    [2.0, 3.0],
    [4.0, 5.0],
    [6.0, 7.0]])
    print(m1 * m2)
    m1 = Matrix([[0.0, 1.0, 2.0],
    [0.0, 2.0, 4.0]])
    v1 = Vector([[1], [2], [3]])
    print(m1 * v1)
    v1 = Vector([[1], [2], [3]])
    v2 = Vector([[2], [4], [8]])
    print(v1 + v2)

def main():
    #matrix_creation_test()
    #matrix_addition_test()
    #matrix_substraction_test()
    #matrix_div_test()
    #matrix_mul_test()
    #vector_test()
    subject_test()
    
if __name__ == "__main__":
    main()