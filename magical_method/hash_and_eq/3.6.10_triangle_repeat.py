class Vertex:
    @classmethod
    def chek(cls, value):
        if not isinstance(value, (int, float)):
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.chek(value)
        return setattr(instance, self.name, value)


class Triangle:
    a = Vertex()
    b = Vertex()
    c = Vertex()

    @classmethod
    def triangle(cls, a, b, c):
        sp = sorted([a, b, c])
        if not (sp[2] < sp[0] + sp[1]):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.triangle(a, b, c)

    def __len__(self):
        return int(self.a+self.b+self.c)

    def __call__(self, *args, **kwargs):
        p = len(self)/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5


if __name__ == '__main__':
    tr = Triangle(5, 4, 3)
    assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

    try:
        tr = Triangle(-5, 4, 3)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        tr = Triangle(10, 1, 1)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    tr = Triangle(5, 4, 3)
    assert len(tr) == 12, "функция len вернула неверное значение"
    assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"

