import numpy as np

def simple_predict(x: np.ndarray, theta: np.ndarray) -> np.ndarray:

    if type(x) != np.ndarray or type(theta) != np.ndarray or len(x) == 0 or len(theta) != 2:
        return None
    y_hat = np.zeros(len(x))
    for i in range(0, len(x)):
        y_hat[i] = theta[0] + x[i] * theta[1]
    return y_hat