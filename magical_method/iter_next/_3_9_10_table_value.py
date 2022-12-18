class Cell:
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self._table = tuple(tuple(Cell(0) for _ in range(self.cols)) for _ in range(self.rows))

    def _check_type(self, value):
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')

    def _check_coord(self, coord):
        x, y = coord
        if not (isinstance(x, int) and isinstance(y, int) and 0 <= x <= self.rows and 0 <= y <= self.cols):
            raise IndexError('неверный индекс')

    def __iter__(self):
        for row in self._table:
            yield (x.data for x in row)

    def __setitem__(self, key, value):
        self._check_coord(key)
        self._check_type(value)
        x, y = key
        self._table[x][y].data = value

    def __getitem__(self, item):
        self._check_coord(item)
        x, y = item
        return self._table[x][y].data


if __name__ == '__main__':
    tb = TableValues(3, 2)
    n = m = 0
    for row in tb:
        n += 1
        for value in row:
            m += 1
            assert type(
                value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

    assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

    tb[0, 0] = 10
    assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

    try:
        tb[2, 0] = 5.2
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError"

    try:
        a = tb[2, 4]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"
