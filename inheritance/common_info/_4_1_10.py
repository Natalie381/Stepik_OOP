class Vector:
    def __init__(self, *args):
        self.coords = [*args]

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


    def __sub__(self, other):
        self._check(other)
        return Vector(*[x - y for x, y in zip(self.coords, other.coords)])