class Rect:
    def __init__(self, x, y, height, width):
        self.height = height
        self.width = width

    def __hash__(self):
        return hash((self.width, self.height))


if __name__ == '__main__':
    r1 = Rect(10, 5, 100, 50)
    r2 = Rect(-10, 4, 100, 50)

    h1, h2 = hash(r1), hash(r2)
    assert h1 == h2
