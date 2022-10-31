class Matrix:
    data= None
    shape = None


    def __init__(self, arg) -> None:
        self.check_arg(arg)
        if isinstance(arg, list):
            self.data = arg
            self.shape = (len(self.data), len(self.data[0]))
        else:
            self.shape = arg
            self.data = []
            for i in range(0, self.shape[0]):
                self.data.append([0] * self.shape[1])

    def check_arg(self, arg):
        if not isinstance(arg, (list, tuple)):
            raise ValueError(f"unsupported argument format: {arg}")
        if isinstance(arg, list):
            l = len(arg[0])
            for row in arg:
                if not isinstance(row, list) or l != len(row) or not all(isinstance(elem, (int, float)) for elem in row):
                    raise ValueError(f"unsupported argument format: {arg}")
        else:
            if len(arg) != 2:
                raise ValueError(f"unsupported argument format: {arg}")
            elif not isinstance(arg[0], (int, float)) or not isinstance(arg[1],(int, float)):
                raise ValueError(f"unsupported argument format: {arg}")
            elif arg[0] <= 0 or arg[1] <= 0:
                raise ValueError(f"unsupported argument format: {arg}")


    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise NotImplementedError(f"cannot add a {type(other)} to a Matrix")
        elif self.shape != other.shape:
            raise ValueError(f"try to add two matrices with differents sizes")
        try:
            res = type(self)(self.shape)
            for i in range(0, self.shape[0]):
                for j in range(0, self.shape[1]):
                    res.data[i][j] = self.data[i][j] + other.data[i][j]
            return res
        except:
            raise ValueError("Error encountered")
    
    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise NotImplementedError(f"cannot do a sub with a(n) {type(other)} and a Matrix")
        elif self.shape != other.shape:
            raise ValueError(f"try to sub two matrices with differet size")
        try:
            res = type(self)(self.shape)
            for i in range(0, self.shape[0]):
                for j in range(0, self.shape[1]):
                    res.data[i][j] = self.data[i][j] - other.data[i][j]
            return res
        except:
            raise ValueError("Error encountered")
    
    def __rsub__(self, other):
        if not isinstance(other, Matrix):
            raise NotImplementedError(f"cannot do a sub with a(n) {type(other)} and a Matrix")
        elif self.shape != other.shape:
            raise ValueError(f"try to sub two matrices with differet size")
        try:
            res = type(self)(self.shape)
            for i in range(0, self.shape[0]):
                for j in range(0, self.shape[1]):
                    res.data[i][j] = other.data[i][j] - self.data[i][j]
            return res
        except:
            raise ValueError("Error encountered")

    def __truediv__(self, scalar):
        if type(scalar) != int and type(scalar) != float:
            raise NotImplementedError(f"cannot div a Matrix by a {type(scalar)}")
        elif scalar == 0:
            raise ZeroDivisionError(f"cannot div a Matrix by 0")
        res: list = []
        for i in range(0, self.shape[0]):
            row: list = [] 
            for j in range(0, self.shape[1]):
                row.append(self.data[i][j] / scalar)
            res.append(row)
        return type(self)(res)
    
    def __rtruediv__(self, scalar):
        return self / scalar


    def __mul__(self, other):
        print(type(self))
        if type(other) == Vector and (self.shape[1] != other.shape[0] and self.shape[1] != other.shape[1]):
            raise ValueError(f"cannot mul two incompatible matrices and vector")
        elif type(other) == Matrix and (self.shape[0] != other.shape[1] or self.shape[1] != other.shape[0]):
            raise ValueError(f"cannot mul two incompatible matrices")
        res: list = []
        if type(other) == Matrix or type(other) == Vector:
            if type(other) == Vector and self.shape[1] != other.shape[0]:
                other = other.T()
            print(other.shape)
            for i in range(0, self.shape[0]):
                res.append([0] * other.shape[1])
                for j in range(0, other.shape[1]):
                    for k in range(0, self.shape[1]):
                        res[i][j] = res[i][j] + self.data[i][k] * other.data[k][j]
        elif type(other) == int or type(other) == float:
            for i in range(0, self.shape[0]):
                row: list = [] 
                for j in range(0, self.shape[1]):
                    row.append(self.data[i][j] * other)
                res.append(row)
        return type(self)(res)
                   

    def __rmul__(self, other):
        return self * other

    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return f"Matrix({str(self.data)})"

    def T(self):
        res: list = []
        for i in range(0, self.shape[1]):
            row: list = [] 
            for j in range(0, self.shape[0]):
                row.append(self.data[j][i])
            res.append(row)
        return type(self)(res)


class Vector(Matrix):
    def __init__(self, arg) -> None:
        super().__init__(arg)
        if self.shape[0] != 1 and self.shape[1] != 1:
            raise ValueError(f"wrong dimensions for Vector")
