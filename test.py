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
    print("<*** Division test")
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



def main():
    #matrix_creation_test()
    #matrix_addition_test()
    #matrix_substraction_test()
    matrix_div_test()


if __name__ == "__main__":
    main()

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

    v = Vector([[1], [2], [3]])
    m1 = Matrix([[0.0, 1.0, 2.0],
[0.0, 2.0, 4.0]])
    print(m1 * v)
