import numpy as np

def simple_predict(x: np.ndarray, theta: np.ndarray) -> np.ndarray:
    try:
        if type(x) != np.ndarray or type(theta) != np.ndarray or len(x) == 0 or len(theta) != 2:
            return None
        y_hat = np.zeros(len(x))
        for i in range(0, len(x)):
            y_hat[i] = theta[0] + x[i] * theta[1]
        return y_hat
    except:
        return None


def main_test():
    x = np.arange(1,6)
    # Example 1:
    theta1 = np.array([5, 0])
    print(simple_predict(x, theta1))
    # Example 2:
    theta2 = np.array([0, 1])
    print(simple_predict(x, theta2))
    # Do you understand why y_hat == x here?
    # Example 3:
    theta3 = np.array([5, 3])
    print(simple_predict(x, theta3))
    # Example 4:
    theta4 = np.array([-3, 1])
    print(simple_predict(x, theta4))

if __name__ == "__main__":
    main_test()