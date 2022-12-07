from random import randint


class Cell:
    def __init__(self):
        self._is_mine = False
        self._number = 0  # число мин вокруг клетки
        self._is_open = False  # закоыта или открыта клетка

    @property
    def is_mine(self):
        return self._is_mine

    @is_mine.setter
    def is_mine(self, value):
        if isinstance(value, bool):
            self._is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if isinstance(value, int) and value in range(0, 9):
            self._number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self._is_open

    @is_open.setter
    def is_open(self, value):
        if isinstance(value, bool):
            self._is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return not self._is_open


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __del__(self):
        GamePole.__instance = None

    def __init__(self, N: int, M: int, total_mines: int):
        self.__pole_cells = [[Cell() for _ in range(M)] for _ in range(N)]
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self._open_cell = []
        self.list_show = [['*'] * self.M for _ in range(self.N)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        '''Расставляет мины на поле'''
        self.list_coords_mins = [(randint(0, self.N - 1), randint(0, self.M - 1)) for _ in range(self.total_mines)]  # список координат мин
        # while len(set(self.list_coords_mins)) <= self.total_mines:
        #     self.list_coords_mins.append((randint(0, self.N - 1), randint(0, self.M - 1)))

        for coord in self.list_coords_mins:
            x, y = coord[0], coord[1]
            self.pole[x][y].is_mine = True  # ахождение ячейки с миной
            for i in range(max(0, x - 1), min(self.N , x + 2)):
                for j in range(max(0, y - 1), min(self.M , y + 2)):
                    self.pole[i][j].number = min(self.pole[i][j].number + 1, 8)

    def open_cell(self, i: int, j: int):
        '''Функция, открывающая ячейку'''
        if not (isinstance(i, int) and isinstance(j, int) and i in range(0, self.N) and j in range(0, self.M)):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True
        if self.pole[i][j].is_mine:
            self.list_show[i][j] = '#'
        else:
            self.list_show[i][j] = self.pole[i][j].number

    def show_pole(self):
        '''Функция для отображения поля'''
        for i in self.list_show:
            print(*i)


if __name__ == '__main__':
    p1 = GamePole(10, 20, 10)
    p2 = GamePole(10, 20, 10)
    assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
    p = p1

    cell = Cell()
    assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
        Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

    cell.is_mine = True
    cell.number = 5
    cell.is_open = True
    assert bool(cell) == False, "функция bool() вернула неверное значение"

    try:
        cell.is_mine = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        cell.number = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    p.init_pole()
    m = 0
    for row in p.pole:
        for x in row:
            assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
            if x.is_mine:
                m += 1

    assert m == 10, "на поле расставлено неверное количество мин"
    p.open_cell(0, 1)
    p.open_cell(9, 19)

    try:
        p.open_cell(10, 20)
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"


    def count_mines(pole, i, j):
        n = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                ii, jj = k + i, l + j
                if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                    continue
                if pole[ii][jj].is_mine:
                    n += 1

        return n


    for i, row in enumerate(p.pole):
        for j, x in enumerate(row):
            if not p.pole[i][j].is_mine:
                m = count_mines(p.pole, i, j)
                assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"
