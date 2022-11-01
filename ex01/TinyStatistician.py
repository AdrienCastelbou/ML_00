from math import sqrt
import numpy as np
from typing import Union

class TinyStatistician:
    def mean(self, x: Union[list, np.array]) -> float:
        try:
            l = float(len(x))
            sum = 0.0
            for elem in x:
                if not isinstance(elem, (float, int)):
                    return None
                sum += elem
            return sum / l
        except:
            return None


    def median(self, x: Union[list, np.array])  -> float:
        try:
            l = len(x)
            if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
                return None
            x.sort()
            return x[int((l + 1) / 2) - 1]
        except:
            return None


    def quartile(self, x: Union[list, np.array]):
        try:
            l = len(x)
            if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
                return None
            x.sort()
            return [float(x[int((l + 3)/ 4) - 1]), float(x[int((3 * l + 1) / 4) - 1])]
        except:
            return None


    def percentile(self, x: Union[list, np.array], p: Union[int, float]) -> float:
        try:
            l = len(x)
            if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
                return None
            x.sort()
            r = (p/100) * (l - 1) + 1
            ri = int(r)
            rf = r - int(r)
            if ri >= l:
                return x[l - 1]
            return x[ri - 1] + rf * (x[ri] - x[ri - 1])
        except:
            return None


    def var(self, x: Union[list, np.array]) -> float:
        try:
            l = len(x)
            if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
                return None
            mean = self.mean(x)
            sum = 0
            for elem in x:
                sum += (elem - mean) * (elem - mean)
            return sum / (l  - 1)
        except:
            return None


    def std(self, x: Union[list, np.array]) -> float:
        try:
            l = len(x)
            if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
                return None
            return sqrt(self.var(x))
        except:
            return None