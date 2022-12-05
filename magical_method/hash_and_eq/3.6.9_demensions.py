class Demensions:
    @classmethod
    def check(cls, *args):
        if not all([i >= 0 for i in args]):
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __init__(self, a: (int | float), b: (int | float), c: (int | float)):
        self.check(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))


if __name__ == '__main__':
    s_inp = "1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"
    lst_dim = []
    for dem in s_inp.split(';'):
        a, b, c = map(float, dem.split())
        lst_dim.append(Demensions(a, b, c))
    lst_dim.sort(key=lambda x: hash(x))
    print(lst_dim)
