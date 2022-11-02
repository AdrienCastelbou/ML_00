import numpy as np

def predict_(x, theta) -> np.array:
    try:
        if type(x) != np.ndarray or type(theta) != np.ndarray:
            return None
        if not len(x) or theta.shape != (2, 1):
            return None
        if x.ndim == 1:
            x = x.reshape(x.shape[0], -1)
        if x.shape[1] != 1:
            return None
        m = np.hstack((np.ones((x.shape[0], 1)), x))
        return m.dot(theta)
    except:
        None

def main_test():
    x = np.arange(1,6)
    # Example 1:
    theta1 = np.array([[5], [0]])
    print(predict_(x, theta1))
    # Do you remember why y_hat contains only 5’s here?
    # Example 2:
    theta2 = np.array([[0], [1]])
    predict_(x, theta2)
    # Do you remember why y_hat == x here?
    # Example 3:
    theta3 = np.array([[5], [3]])
    print(predict_(x, theta3))
    # Example 4:
    theta4 = np.array([[-3], [1]])
    print(predict_(x, theta4))


if __name__ == "__main__":
    main_test()