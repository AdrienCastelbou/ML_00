import numpy as np

def add_intercept(x: np.ndarray):
    try:
        if type(x) != np.ndarray or x.shape[0] == 0:
            return None
        if (len(x.shape) == 1):
            x = x.reshape(x.shape[0], -1)
        intercept = np.ones((x.shape[0], 1))
        extend = np.hstack((intercept, x))
        return extend
    except:
        return None