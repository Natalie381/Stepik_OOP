class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self._dict_of_values = {}

    def new_rows_cols(self):
        ''' Перерасчет значений столбцов и строк при добавлении или удалее'''
        self.rows = max(x[0] for x in self._dict_of_values.keys()) + 1
        self.cols = max(x[1] for x in self._dict_of_values.keys()) + 1

    def add_data(self, row: int, col: int, data):
        self._dict_of_values[(row, col)] = data
        self.new_rows_cols()

    def remove_data(self, row: int, col: int):
        if (row, col) not in self._dict_of_values:
            raise IndexError('ячейка с указанными индексами не существует')
        del self._dict_of_values[(row, col)]
        self.new_rows_cols()

    def __getitem__(self, item):
        x, y = item
        if (x, y) not in self._dict_of_values:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self._dict_of_values[(x, y)].value

    def __setitem__(self, key, value):
        x, y = key
        self._dict_of_values[(x, y)] = Cell(value)
        self.new_rows_cols()


class Cell:
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    st = SparseTable()
    st.add_data(2, 5, Cell("cell_25"))
    st.add_data(0, 0, Cell("cell_00"))
    # st[2, 5] = 25  # изменение значения существующей ячейки
    st[11, 7] = 'cell_117'  # создание новой ячейки
    print(st[0, 0])  # cell_00
    st.remove_data(2, 5)
    print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
    # val = st[2, 5]  # ValueError
    # st.remove_data(12, 3)  # IndexError
