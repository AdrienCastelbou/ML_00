import numpy as np
from math import sqrt

def mse_elem_(y, y_hat):
    J_elem = np.zeros(y.shape[0])
    for i in range(0, y.shape[0]):
        J_elem[i] = (y_hat[i] - y[i]) ** 2
    return J_elem


def mse_(y, y_hat):
    J_elem = mse_elem_(y, y_hat)
    sum = 0
    for elem in J_elem:
        sum += elem
    J = ((1 / y.shape[0])) * sum
    return J


def rmse_(y, y_hat):
    return sqrt(mse_(y, y_hat))
     
def mae_(y, y_hat):
    return (1 / y.shape[0]) * np.sum(np.abs(y_hat - y))

def r2score(y, y_hat):
    return 1 - (np.sum((y_hat - y) ** 2) / np.sum((y - np.mean(y)) ** 2))

def main_test():
    x = np.array([0, 15, -9, 7, 12, 3, -21])
    y = np.array([2, 14, -13, 5, 12, 4, -19])
    # Mean squared error
    ## your implementation
    print(mse_(x,y))
    print(rmse_(x,y))
    print(mae_(x,y))
    print(r2score(x, y))


if __name__ == "__main__":
    main_test()