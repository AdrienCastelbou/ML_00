from math import sqrt
from numpy import array

class TinyStatistician:
    def mean(self, x):
        if type(x) != list and type(x) != array:
            return None
        l = float(len(x))
        sum = 0.0
        for elem in x:
            if not isinstance(elem, (float, int)):
                return None
            sum += elem
        return sum / l
    
    def median(self, x):
        if type(x) != list and type(x) != array:
            return None
        l = len(x)
        if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
            return None
        x.sort()
        return x[int((l + 1) / 2) - 1]
    
    def quartile(self, x):
        if type(x) != list and type(x) != array:
            return None
        l = len(x)
        if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
            return None
        x.sort()
        return [x[int((l + 3)/ 4) - 1], x[int((3 * l + 1) / 4)] - 1]
    
    def percentile(self, x):
        return None
    
    def var(self, x):
        if type(x) != list and type(x) != array:
            return None
        l = len(x)
        if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
            return None
        mean = self.mean(x)
        sum = 0
        for elem in x:
            sum += (elem - mean) * (elem - mean)
        return sum / l
    
    def std(self, x):
        if type(x) != list and type(x) != array:
            return None
        l = len(x)
        if l == 0 or not all(isinstance(elem, (int, float)) for elem in x):
            return None
        return sqrt(self.var(x))

t = TinyStatistician()

print(t.std([2, 7, 3, 12, 9]))
