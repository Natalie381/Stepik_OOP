class IntegerValue:
    @classmethod
    def chek(cls, value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.chek(value)
        return setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, colls, cell):
        if not cell:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.colls = colls
        self.cell = cell
        self.cells = tuple(tuple(cell() for _ in range(colls)) for _ in range(rows))

    def __getitem__(self, item):
        self.check(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.check(key)
        self.cells[key[0]][key[1]].value = value

    def check(self, item):
        if not (isinstance(item[0], int) and isinstance(item[1], int )and 0 <= item[0] < self.rows and 0 <= item[1] < self.colls):
            raise IndexError('неверный индекс для доступа к элементам массива')


if __name__ == '__main__':
    table = TableValues(2, 3, cell=CellInteger)
    print(table[0, 1])
    table[1, 1] = 10
    # table[0, 0] = 1.45  # генерируется исключение ValueError

    # вывод таблицы в консоль
    for row in table.cells:
        for x in row:
            print(x.value, end=' ')
        print()