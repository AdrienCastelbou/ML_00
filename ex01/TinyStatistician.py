from math import sqrt
import numpy as np
from typing import Union

class TinyStatistician:
    def mean(self, x: Union[list, np.array]) -> float:
        try:
            l = len(x)
            res = 0.0
            for elem in x:
                if not isinstance(elem, (float, int)):
                    return None
                res += elem
            return res / l
        except:
            return None


    def median(self, x: Union[list, np.array]) -> float:
        try:
            sorted_x = sorted(x)
            l = len(x)
            if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
                return None
            if l % 2:
                return sorted_x[int(len(x) / 2)]
            else:
                return (sorted_x[int(len(x) / 2) - 1] + sorted_x[int(len(x) / 2)]) / 2
        except:
            return None


    def quartile(self, x: Union[list, np.array]):
        try:
            l = len(x)
            if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
                return None
            x = sorted(x)
            print(x)
            return [float(x[int(l / 4)]), float(x[int(l * 3 / 4)])]
        except:
            return None


    def percentile(self, x: Union[list, np.array], p: Union[int, float]) -> float:
        try:
            l = len(x)
            sorted_x = sorted(x)
            idx = int(np.ceil(p / 100 * l)) - 1
            return sorted_x[idx]
        except:
            return None


    def var(self, x: Union[list, np.array]) -> float:
        try:
            l = len(x)
            if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
                return None
            mean = self.mean(x)
            res = 0
            for elem in x:
                res += (elem - mean) * (elem - mean)
            return res / (l  - 1)
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