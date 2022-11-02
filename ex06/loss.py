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


def loss_elem_(y, y_hat):
    if type(y) != np.ndarray or type(y_hat) != np.ndarray:
        return None
    if y.ndim == 1:
        y = y.reshape(y.shape[0], -1)
    if y_hat.ndim == 1:
        y_hat = y_hat.reshape(y_hat.shape[0], -1)
    if y.shape[1] != 1 or y_hat.shape[1] != 1:
        return None
    try:
        J_elem = np.zeros(y.shape[0])
        for i in range(0, y.shape[0]):
            J_elem[i] = (y_hat[i] - y[i]) ** 2
        return J_elem
    except:
        return None


def loss_(y, y_hat):
    if type(y) != np.ndarray or type(y_hat) != np.ndarray:
        return None
    if y.ndim == 1:
        y = y.reshape(y.shape[0], -1)
    if y_hat.ndim == 1:
        y_hat = y_hat.reshape(y_hat.shape[0], -1)
    if y.shape[1] != 1 or y_hat.shape[1] != 1:
        return None
    try:
        J_elem = loss_elem_(y, y_hat)
        sum = 0
        for elem in J_elem:
            sum += elem
        J = (1 / (2 * y.shape[0])) * sum
        return J
    except:
        return None


def main_test():
    x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    y_hat1 = predict_(x1, theta1)
    y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
    # Example 1:
    print(loss_elem_(y1, y_hat1))
    print(loss_(y1, y_hat1))
    x2 = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(-1, 1)
    theta2 = np.array([[0.], [1.]]).reshape(-1, 1)
    y_hat2 = predict_(x2, theta2)
    y2 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)
    # Example 3:
    loss_(y2, y_hat2)
    print(loss_(y2, y_hat2))
    print(loss_(y2, y2))

if __name__ == "__main__":
    main_test()