import numpy as np
import matplotlib.pyplot as plt

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


def plot(x, y, theta):
    if type(y) != np.ndarray or type(x) != np.ndarray or type(theta) != np.ndarray:
        return None
    if y.ndim == 1:
        y = y.reshape(y.shape[0], -1)
    if x.ndim == 1:
        x = x.reshape(x.shape[0], -1)
    if theta.ndim == 1:
        theta = theta.reshape(theta.shape[0], -1)
    if y.shape[1] != 1 or x.shape[1] != 1 or theta.shape != (2, 1):
        return None
    try:
        if type(y) != np.ndarray or len(y) == 0:
            return
        if y.ndim == 1:
            y = y.reshape(x.shape[0], -1)
        if y.shape[1] != 1:
            return
        y_hat = predict_(x, theta)
        plt.scatter(x, y)
        plt.plot(x, y_hat, color="red")
        plt.show()
    except:
        return


def main_test():
    x = np.arange(1,6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
    # Example 1:
    theta1 = np.array([[4.5],[-0.2]])
    plot(x, y, theta1)

    theta2 = np.array([[-1.5],[2]])
    plot(x, y, theta2)

    theta3 = np.array([[3],[0.3]])
    plot(x, y, theta3)

if __name__ == "__main__":
    main_test()