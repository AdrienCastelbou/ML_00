from math import sqrt
import numpy as np
from typing import Union

class TinyStatistician:
    def mean(self, x: Union[list, np.array]) -> float:
        l = float(len(x))
        sum = 0.0
        for elem in x:
            if not isinstance(elem, (float, int)):
                return None
            sum += elem
        return sum / l
    
    def median(self, x: Union[list, np.array])  -> float:
        l = len(x)
        if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
            return None
        x.sort()
        return x[int((l + 1) / 2) - 1]
    
    def quartile(self, x: Union[list, np.array]):
        l = len(x)
        if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
            return None
        x.sort()
        return [float(x[int((l + 3)/ 4) - 1]), float(x[int((3 * l + 1) / 4) - 1])]
    

    def percentile(self, x: Union[list, np.array], p: Union[int, float]) -> float:
        l = len(x)
        if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
            return None
        x.sort()
        return None
    
    def var(self, x: Union[list, np.array]) -> float:
        l = len(x)
        if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
            return None
        mean = self.mean(x)
        sum = 0
        for elem in x:
            sum += (elem - mean) * (elem - mean)
        return sum / (l  - 1)
    
    def std(self, x: Union[list, np.array]) -> float:
        l = len(x)
        if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
            return None
        return sqrt(self.var(x))

a = [1, 42, 300, 10, 59]
#print(TinyStatistician().mean(a))
#print(TinyStatistician().median(a))
#print(TinyStatistician().quartile(a))
print(TinyStatistician().percentile(a, 10))
#print(TinyStatistician().percentile(a, 15))
#print(TinyStatistician().percentile(a, 20))
#print(TinyStatistician().var(a))
#print(TinyStatistician().std(a))
