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