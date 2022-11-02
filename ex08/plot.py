import numpy as np
import matplotlib.pyplot as plt

def loss_(y, y_hat):
    return float(1 / (2 * y.shape[0]) * (y_hat - y).T.dot(y_hat - y))

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


def plot_with_loss(x, y, theta):
    if type(y) != np.ndarray or type(y_hat) != np.ndarray or type(theta) != np.ndarray:
        return None
    if y.ndim == 1:
        y = y.reshape(y.shape[0], -1)
    if y_hat.ndim == 1:
        y_hat = y_hat.reshape(y_hat.shape[0], -1)
    if theta.ndim == 1:
        theta = theta.reshape(theta.shape[0], -1)
    if y.shape[1] != 1 or y_hat.shape[1] != 1 or theta.shape != (2, 1):
        return None
    try:
        y_hat = predict_(x, theta)
        plt.scatter(x, y)
        plt.title(f"Cost: {2 * loss_(y, y_hat)}")
        plt.plot(x, y_hat, color="orange")
        for i in range(0, y.shape[0]):
            plt.plot([x[i], x[i]], [y[i][0], y_hat[i][0]], 'r', linestyle="--")
        plt.show()
    except:
        return 



def main_test():
    x = np.arange(1,6)
    y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
    theta1= np.array([18,-1]) 
    plot_with_loss(x, y, theta1)
    theta2 = np.array([14, 0])
    plot_with_loss(x, y, theta2)
    theta3 = np.array([12, 0.8])
    plot_with_loss(x, y, theta3)

if __name__ == "__main__":
    main_test()