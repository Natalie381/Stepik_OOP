class Array:
    def __init__(self, max_lenth, cell):
        self.max_lenth = max_lenth
        self.cell = cell
        self.__value = [cell() for _ in range(max_lenth)]

    def __getitem__(self, item):
        self.check(item)
        return self.__value[item].value

    def __setitem__(self, key, value):
        self.check(key)
        self.__value[key] = self.cell(value)

    def __repr__(self):
        return ' '.join([str(x.value) for x in self.__value])

    def check(self, item):
        if not (isinstance(item, int) and 0 <= item < self.max_lenth):
            raise IndexError('неверный индекс для доступа к элементам массива')


class Integer:
    def __init__(self, start_value=0):
        self.__value = 0
        self.value = start_value

    def check(self, value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.check(value)
        self.__value = value

if __name__ == '__main__':
    ar_int = Array(10, cell=Integer)
    print(ar_int[3])
    print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
    ar_int[1] = 10
    # ar_int[1] = 10.5  # должно генерироваться исключение ValueError
    # ar_int[10] = 1  # должно генерироваться исключение IndexError
    print(ar_int)