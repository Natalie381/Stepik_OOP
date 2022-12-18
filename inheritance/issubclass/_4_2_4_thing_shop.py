class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __eq__(self, other):
        return hash(self) == hash(other)


class DictShop(dict):
    def _check_keys(self, thing):
        if not isinstance(thing, Thing) and not (isinstance(thing, dict) and all(isinstance(x, Thing) for x in thing)):
            raise TypeError('ключами могут быть только объекты класса Thing')

    def __init__(self, *args):
        if not args:
            super().__init__()
        else:
            self._check_keys(thing)
            super().__init__(thing)

    def __setitem__(self, key, value):
        self._check_keys(key)
        super().__setitem__(key, value)


if __name__ == '__main__':
    th_1 = Thing('Лыжи', 11000, 1978.55)
    th_2 = Thing('Книга', 1500, 256)
    dict_things = DictShop()
    dict_things[th_1] = th_1
    dict_things[th_2] = th_2

    for x in dict_things:
        print(x.name)

    # dict_things[1] = th_1  # исключение TypeError
