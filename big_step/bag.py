class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.total_weight = 0
        self.list_of_thing = []

    def check_weight(self, weight_new_thing):
        if self.total_weight + weight_new_thing > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing):
        self.check_weight(thing.weight)
        self.list_of_thing.append(thing)
        self.total_weight += thing.weight

    def check_indx(self, indx):
        if not (isinstance(indx, int) and 0 <= indx < len(self.list_of_thing)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_indx(item)
        return self.list_of_thing[item]

    def __setitem__(self, key, value):
        self.check_weight(value.weight - self[key].weight)
        self.total_weight += value.weight - self[key].weight
        self.list_of_thing[key] = value

    def __delitem__(self, key):
        self.total_weight -= self[key].weight
        del self.list_of_thing[key]




class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

if __name__ == '__main__':
    bag = Bag(1000)
    bag.add_thing(Thing('книга', 100))
    bag.add_thing(Thing('носки', 200))
    bag.add_thing(Thing('рубашка', 500))
    # bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
    print(bag[2].name)  # рубашка
    bag[1] = Thing('платок', 100)
    print(bag[1].name)  # платок
    del bag[0]
    print(bag[0].name)  # платок
    # t = bag[4]  # генерируется исключение IndexError