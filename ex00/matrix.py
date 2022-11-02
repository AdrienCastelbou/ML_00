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
        if not isinstance(scalar, (int, float)):
            raise NotImplementedError(f"cannot div a Matrix by a {type(scalar)}")
        elif scalar == 0:
            raise ZeroDivisionError(f"cannot div a Matrix by 0")
        try:
            res = type(self)(self.shape)
            for i in range(0, self.shape[0]):
                for j in range(0, self.shape[1]):
                    res.data[i][j] = self.data[i][j] / scalar
            return res
        except:
            raise ValueError("Error encountered")
    
    def __rtruediv__(self, scalar):
        raise NotImplementedError(f"cannot div a {type(scalar)} by a Matrix")

    def __mul__(self, other):
        if (not isinstance(other, (Matrix, Vector, int, float))):
            raise NotImplementedError(f"cannot mul a {type(other)} and a Matrix")
        if type(other) == Vector and self.shape[1] != other.shape[0]:
            raise ValueError(f"cannot mul two incompatible matrices and vector")
        elif type(other) == Matrix and (self.shape[0] != other.shape[1] or self.shape[1] != other.shape[0]):
            raise ValueError(f"cannot mul two incompatible matrices")
        if (isinstance(other, (Matrix, Vector))):
            try:
                res = type(self)((self.shape[0], other.shape[1]))
                for i in range(0, self.shape[0]):
                    for j in range(0, other.shape[1]):
                        for k in range(0, self.shape[1]):
                            res.data[i][j] += self.data[i][k] * other.data[k][j]
                return res
            except:
                raise ValueError("Error encountered")  
        elif (isinstance(other, (int, float))):
            try:
                res = type(self)(self.shape)
                for i in range(0, self.shape[0]):
                    for j in range(0, self.shape[1]):
                        res.data[i][j] = self.data[i][j] * other
                return res
            except:
                raise ValueError("Error encountered")

    def __rmul__(self, other):
        if (isinstance(other, (int, float))):
            return self * other
        raise NotImplementedError(f"cannot mul a {type(other)} and a Matrix")

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

    
    def __mul__(self, other):
        if not isinstance(other, (Matrix, Vector, int, float)):
            raise NotImplementedError(f"cannot mul a {type(other)} and a Matrix")
        elif type(other) == Vector and self.shape != other.shape:
            raise ValueError(f"cannot mul two incompatible vectors")
        elif type(other) == Matrix and self.shape[1] != other.shape[0]:
            raise ValueError(f"cannot mul two incompatible matrices and vector")
        if type(other) == Matrix:
            try:
                res = type(self)((self.shape[0], other.shape[1]))
                for i in range(0, self.shape[0]):
                    for j in range(0, other.shape[1]):
                        for k in range(0, self.shape[1]):
                            res.data[i][j] += self.data[i][k] * other.data[k][j]
                return res
            except:
                raise ValueError("Error encountered")
        elif type(other) == Vector:
            try:
                is_row = True if self.shape[0] == 1 else False
                r_self = self if is_row else self.T()
                r_other = other if is_row else other.T()
                res = type(self)(r_self.shape)
                for i in range(0, r_self.shape[1]):
                    for j in range(0, r_self.shape[1]):
                        if j != i:
                            for k in range(0, r_self.shape[1]):
                                if k != i:
                                    if k > j:
                                        res.data[0][i] += r_self.data[0][j]* r_other.data[0][k]
                                    elif k < j:
                                        res.data[0][i] -= r_self.data[0][j]* r_other.data[0][k]
                return res if is_row else res.T()
            except:
                raise ValueError("Error encountered")
        elif (isinstance(other, (int, float))):
            return super().__mul__(other)

    def dot(self, v):
        if not isinstance(v, Vector):
            raise ValueError("incompatible type")
        if (self.shape != v.shape):
            raise ValueError("Invalid dimensions")
        sum = 0
        for i in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
                sum += self.data[i][j] * v.data[i][j]
        return sum
