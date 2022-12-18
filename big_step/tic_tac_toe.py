class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0
                cell.is_free = True

    def check_coords(self, coord):
        for value in coord
            if not (isinstance(value, int) and 0 <= value <= 2) or not (isinstance(value, slice)):
                raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        self.check_coords(item)
        x, y = item
        if all(isinstance(i, int) for i in item):
            return self.pole[x][item[y]].value
        if type(x) is int:
            retu

    def __setitem__(self, key, value):
        self.check_coords(key)
        if self.pole[key]:
            self.pole[key] = value
        else:
            raise ValueError('клетка уже занята')


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


if __name__ == '__main__':
