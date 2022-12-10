class Vector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def _check(self, other):
        if len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')

    def __eq__(self, other):
        self._check(other)
        return self.coords == other.coords

    def __add__(self, other):
        self._check(other)
        return Vector(*[x + y for x, y in zip(self.coords, other.coords)])

    def __mul__(self, other):
        self._check(other)
        return Vector(*[x * y for x, y in zip(self.coords, other.coords)])

    def __sub__(self, other):
        self._check(other)
        return Vector(*[x - y for x, y in zip(self.coords, other.coords)])

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [x + other for x in self.coords]
        elif isinstance(other, Vector):
            self._check(other)
            self.coords = [x + y for x, y in zip(self.coords, other.coords)]
        return self

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [x * other for x in self.coords]
        elif isinstance(other, Vector):
            self._check(other)
            self.coords = [x * y for x, y in zip(self.coords, other.coords)]
        return self

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [x - other for x in self.coords]
        elif isinstance(other, Vector):
            self._check(other)
            self.coords = [x - y for x, y in zip(self.coords, other.coords)]
        return self

if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print((v1 + v2).coords)  # [5, 7, 9]
    print((v1 - v2).coords)  # [-3, -3, -3]
    print((v1 * v2).coords)  # [4, 10, 18]

    v1 += 10
    print(v1.coords)  # [11, 12, 13]
    v1 -= 10
    print(v1.coords)  # [1, 2, 3]
    v1 += v2
    print(v1.coords)  # [5, 7, 9]
    v2 -= v1
    print(v2.coords)  # [-1, -2, -3]

    print(v1 == v2)  # False
    print(v1 != v2)  # True
