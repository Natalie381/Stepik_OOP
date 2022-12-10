class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self._point = []
        self._speed = []

    def _chek(self, value):
        if not (isinstance(value, int) and 0 <= value < len(self._point)):
            raise IndexError('некорректный индекс')

    def add_point(self, x, y, speed):
        self._point.append((x, y))
        self._speed.append(speed)

    def __getitem__(self, item):
        self._chek(item)
        return self._point[item], self._speed[item]

    def __setitem__(self, key, value):
        self._chek(key)
        self._speed[key] = value


if __name__ == '__main__':
    tr = Track(10, -5.4)
    tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
    tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
    tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

    tr[2] = 60
    c, s = tr[2]
    print(c, s)

    # res = tr[3]
